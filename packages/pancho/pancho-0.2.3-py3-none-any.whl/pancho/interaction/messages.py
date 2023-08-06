import collections.abc
import datetime
import dataclasses
import typing

from ..definitions import contracts

UNSET = typing.cast(None, object())


def dump_payload(obj: contracts.Message, exclude_unset=True):
    return {
        k: v
        for k, v in obj.__dict__.items()
        if k not in ('id', 'actor_id', 'created_at') and not (exclude_unset and v is UNSET)
    }


def dump_message(obj: contracts.Message):
    return dataclasses.asdict(obj)


@dataclasses.dataclass(kw_only=True)
class Command(contracts.Command):
    id: contracts.IdentifierType
    actor_id: contracts.IdentifierType
    created_at: datetime.datetime = dataclasses.field(default_factory=datetime.datetime.utcnow)


@dataclasses.dataclass(kw_only=True)
class Event(contracts.Event):
    actor_id: contracts.IdentifierType
    created_at: datetime.datetime = dataclasses.field(default_factory=datetime.datetime.utcnow)


@dataclasses.dataclass(kw_only=True)
class InfoEvent(Event, contracts.InfoEvent):
    pass


@dataclasses.dataclass(kw_only=True)
class ExceptionEvent(Event, contracts.ExceptionEvent):
    code: int
    message: str
    details: collections.abc.Sequence | None = None


@dataclasses.dataclass(kw_only=True)
class UnexpectedError(ExceptionEvent):
    code: int = 500
