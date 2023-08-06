from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class ActorClass(StrEnum):
    NoActor = auto()
    PrimaryScada = auto()
    PrimaryMeter = auto()
    BooleanActuator = auto()
    SimpleSensor = auto()
    HomeAlone = auto()
    Atn = auto()
    MultipurposeSensor = auto()
    Thermostat = auto()

    @classmethod
    def default(cls) -> "ActorClass":
        return cls.NoActor

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]
