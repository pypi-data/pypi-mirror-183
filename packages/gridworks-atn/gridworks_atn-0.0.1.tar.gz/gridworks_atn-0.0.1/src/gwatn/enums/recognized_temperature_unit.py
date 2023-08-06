from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class RecognizedTemperatureUnit(StrEnum):
    C = auto()
    F = auto()

    @classmethod
    def default(cls) -> "RecognizedTemperatureUnit":
        return cls.C

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]
