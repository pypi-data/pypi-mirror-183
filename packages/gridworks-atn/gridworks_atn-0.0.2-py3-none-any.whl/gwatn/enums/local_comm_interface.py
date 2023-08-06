from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class LocalCommInterface(StrEnum):
    ANALOG_4_20_MA = auto()
    RS232 = auto()
    I2C = auto()
    WIFI = auto()
    SIMRABBIT = auto()
    UNKNOWN = auto()
    ETHERNET = auto()
    ONEWIRE = auto()
    RS485 = auto()

    @classmethod
    def default(cls) -> "LocalCommInterface":
        return cls.UNKNOWN

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]
