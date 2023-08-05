import dataclasses
import importlib
import inspect
import re
from collections import defaultdict
from enum import Enum, auto
from inspect import getfile
from pathlib import Path
from types import ModuleType
from typing import (
    Any,
    Dict,
    Iterable,
    List,
    NamedTuple,
    Optional,
    Set,
    Tuple,
    Type,
    Union,
)

from pydantic import NameEmail
from sqlalchemy import Column, MetaData, Table
from sqlalchemy.orm import declared_attr, registry
from sqlalchemy.sql import ColumnCollection

from amora.config import settings
from amora.logger import logger
from amora.protocols import Compilable, CompilableProtocol
from amora.utils import ensure_path, list_files, model_path_for_target_path

metadata = MetaData(schema=f"{settings.TARGET_PROJECT}.{settings.TARGET_SCHEMA}")
mapper_registry = registry(metadata=metadata)

Model = Type["AmoraModel"]
Models = Iterable[Model]

LabelKey = str
LabelValue = str
LabelKeys = Iterable[LabelKey]

SQLALCHEMY_METADATA_KEY = "sa"


def Field(*args, **kwargs):
    return dataclasses.field(
        init=False, metadata={SQLALCHEMY_METADATA_KEY: Column(*args, **kwargs)}
    )


class Label(NamedTuple):
    """
    A label is a (key, value) pair that can also be represented as a "key:value" string. E.g.:

    ```python
    Label("freshness", "daily")
    ```
    """

    key: LabelKey
    value: LabelValue

    def __str__(self):
        return f"{self.key}:{self.value}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if not isinstance(other, str):
            return self.key == other.key and self.value == other.value

        return self == Label.from_str(other)

    @classmethod
    def from_str(cls, label: str):
        """
        >>> Label.from_str("domain:health")
        Label(key="domain", value="health")
        """

        return cls(*label.split(":"))


LabelRepr = Union[Label, str]
Labels = Set[Label]


@dataclasses.dataclass
class PartitionConfig:
    field: str
    data_type: str = "date"
    granularity: str = "day"
    range: Dict[str, Any] = dataclasses.field(default_factory=dict)


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class MaterializationTypes(AutoName):
    ephemeral = auto()
    view = auto()
    table = auto()


Owner = NameEmail


@dataclasses.dataclass
class ModelConfig:
    """
    Model configuration metadata

    Attributes:
        cluster_by (List[str]): BigQuery tables can be [clustered](https://cloud.google.com/bigquery/docs/clustered-tables) to colocate related data. Expects a list of columns, as strings.
        description (Optional[str]): A string description of the model, used for documentation
        labels (Labels): Labels that can be used for data catalog and resource selection
        materialized (amora.models.MaterializationTypes): The materialization configuration: `view`, `table`, `ephemeral`. Default: `view`
        partition_by (Optional[PartitionConfig]): BigQuery supports the use of a [partition by](https://cloud.google.com/bigquery/docs/partitioned-tables) clause to easily partition a table by a column or expression. This option can help decrease latency and cost when querying large tables.
    """

    description: str = "Undocumented! Generated by Amora Data Build Tool 💚"
    materialized: MaterializationTypes = MaterializationTypes.view
    partition_by: Optional[PartitionConfig] = None
    cluster_by: Optional[List[str]] = None
    labels: Labels = dataclasses.field(default_factory=set)
    owner: Optional[Owner] = None

    @property
    def labels_dict(self) -> Dict[str, str]:
        return {label.key: label.value for label in self.labels}


class AmoraModel:
    """
    Attributes:
        __depends_on__ (Models): A list of Amora Models that the current model depends on
        __model_config__ (ModelConfig): Model configuration metadata
        __table__ (Table): SQLAlchemy table object
        __table_args__ (Dict[str, Any]): SQLAlchemy table arguments
        __tablename__override__ (Optional[str]): Set the desired table name. Overrides __tablename__
    """

    __table__: Table
    __tablename__override__: Optional[str] = None
    __depends_on__: Models = []
    __model_config__ = ModelConfig(materialized=MaterializationTypes.view)

    __sa_dataclass_metadata_key__ = SQLALCHEMY_METADATA_KEY
    __table_args__: Dict[str, Any] = {"extend_existing": True}

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        mapper_registry.mapped(dataclasses.dataclass(cls))

    @declared_attr
    def __tablename__(cls: Model) -> str:  # type: ignore
        """
        By default, `__tablename__` is the `snake_case` class name.

        ```python
        class MyModel(AmoraModel):
            ...


        assert MyModel.__tablename__ == "my_model"
        ```
        """

        return (
            cls.__tablename__override__
            or re.sub(r"(?<!^)(?=[A-Z])", "_", cls.__mro__[0].__name__).lower()
        )

    @classmethod
    def columns(cls) -> Optional[ColumnCollection]:
        if cls.__model_config__.materialized == MaterializationTypes.ephemeral:
            cte = cls.source()
            if cte is not None:
                return cte.exported_columns
            else:
                return None
        else:
            return cls.__table__.columns

    @classmethod
    def dependencies(cls) -> List[Table]:
        source = cls.source()
        if source is None:
            return []

        return [other.__table__ for other in cls.__depends_on__]

    @classmethod
    def source(cls) -> Optional[Compilable]:
        """
        Called when `amora compile` is executed, Amora will build this model
        in your data warehouse by wrapping it in a `create view as` or `create table as` statement.

        Return `None` for defining models for tables/views that already exist on the data warehouse
        and shouldn't be managed by Amora.

        Return a `Compilable`, which is a sqlalchemy select statement, in order to compile the model with the given statement
        :return:
        """
        return None

    @classmethod
    def target_path(cls) -> Path:
        # {settings.dbt_models_path}/a_model/a_model.py -> a_model/a_model.py
        strip_path = settings.models_path.as_posix()
        relative_model_path = str(cls.path()).split(strip_path)[1][1:]
        # a_model/a_model.py -> ~/project/amora/target/a_model/a_model.sql
        target_file_path = settings.target_path.joinpath(
            relative_model_path.replace(".py", ".sql")
        )

        return target_file_path

    @classmethod
    def path(cls) -> Path:
        return Path(getfile(cls))

    @classmethod
    def unique_name(cls) -> str:
        return cls.__table__.fullname

    @classmethod
    def owner(cls) -> str:
        if model_owner := cls.__model_config__.owner:
            return str(model_owner)

        return ""


def _is_amora_model(candidate: ModuleType) -> bool:
    return (
        isinstance(candidate, CompilableProtocol)
        and inspect.isclass(candidate)
        and issubclass(candidate, AmoraModel)
        and hasattr(candidate, "__table__")
    )


@ensure_path
def amora_model_for_path(path: Path) -> Model:
    try:
        relative_module_name = (
            path.relative_to(settings.models_path)
            .as_posix()
            .replace("/", ".")
            .replace(".py", "")
        )

        module = importlib.import_module(
            relative_module_name, settings.models_path.name
        )
    except ModuleNotFoundError as e:
        raise ValueError(f"Invalid path `{path}`") from e

    compilables = inspect.getmembers(
        module,
        _is_amora_model,
    )

    for _name, class_ in compilables:
        if class_.path() == path:
            return class_

    raise ValueError(f"Invalid path `{path}`")


def amora_model_for_target_path(path: Path) -> Model:
    model_path = model_path_for_target_path(path)
    return amora_model_for_path(model_path)


def amora_model_for_name(model_name: str) -> Model:
    for m in mapper_registry.mappers:
        if m.class_.unique_name() == model_name:
            return m.class_

    raise ValueError(f"{model_name} not found on models list")


def amora_model_from_name_list(
    model_name_list: Iterable[str],
) -> Iterable[Tuple[Model, Path]]:
    for model, _path in list_models():
        if model.unique_name() in model_name_list:
            yield model, _path


def list_models(
    path: Path = settings.models_path,
) -> Iterable[Tuple[Model, Path]]:
    for model_file_path in list_files(path, suffix=".py"):
        if model_file_path.stem.startswith("_"):
            continue

        try:
            yield amora_model_for_path(model_file_path), model_file_path

        except ValueError:
            logger.exception(
                "Unable to load amora model for path",
                extra={"model_file_path": model_file_path},
            )
            continue


def list_models_with_owner(owner: Union[str, Owner]) -> Iterable[Tuple[Model, Path]]:
    if isinstance(owner, str):
        owner = Owner.validate(owner)

    for model, file_path in list_models():
        if owner == model.__model_config__.owner:
            yield model, file_path


def owners_to_models_dict() -> Dict[str, List[Model]]:
    owners_dict = defaultdict(list)
    for model, _ in list_models():
        owner = model.owner()
        if owner:
            owners_dict[owner].append(model)
    return owners_dict


def select_models_with_labels(labels: Labels) -> Iterable[Tuple[Model, Path]]:
    def matches_labels(item: Tuple[Model, Path]) -> bool:
        model, _model_path = item
        return match_labels(model, labels)

    return filter(matches_labels, list_models())


def select_models_with_label_keys(
    label_keys: LabelKeys,
) -> Iterable[Tuple[Model, Path]]:
    keys = set(label_keys)

    def matches_labels(item: Tuple[Model, Path]) -> bool:
        model, _model_path = item
        return match_label_keys(model, keys)

    return filter(matches_labels, list_models())


def match_label_keys(model: Model, label_keys: Iterable[LabelKey]) -> bool:
    for key in label_keys:
        for label in model.__model_config__.labels:
            if label.key == key:
                return True
    return False


def match_labels(model: Model, labels: Labels) -> bool:
    for label in labels:
        if label in model.__model_config__.labels:
            return True
    return False
