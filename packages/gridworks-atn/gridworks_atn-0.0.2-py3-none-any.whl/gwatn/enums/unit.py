from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class Unit(StrEnum):
    Unknown = auto()
    Unitless = auto()
    W = auto()
    Celcius = auto()
    Fahrenheit = auto()
    Gpm = auto()
    Wh = auto()
    AmpsRms = auto()
    VoltsRms = auto()

    @classmethod
    def default(cls) -> "Unit":
        return cls.Unknown

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]
