import enum
from dataclasses import dataclass
from typing import Any, List, Union

Path = List[Union[str, int]]


@dataclass(frozen=True)
class Add:
    path: Path
    new_value: Any
    stack: str


@dataclass(frozen=True)
class Change:
    path: Path
    old_value: Any
    new_value: Any
    stack: str


@dataclass(frozen=True)
class Delete:
    path: Path
    old_value: Any
    stack: str


Action = Union[Add, Change, Delete]


class ValueSnapshotStrategy(enum.Enum):
    STRING = "string"
    # TODO: others json, deep_string, deep_json


@dataclass(frozen=True)
class TracerOptions:
    value_snapshot_strategy: ValueSnapshotStrategy = ValueSnapshotStrategy.STRING


@dataclass(frozen=True)
class Options:
    tracer: TracerOptions = TracerOptions()
