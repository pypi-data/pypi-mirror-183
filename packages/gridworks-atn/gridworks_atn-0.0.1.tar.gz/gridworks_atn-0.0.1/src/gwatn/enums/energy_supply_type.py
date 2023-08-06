from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class EnergySupplyType(StrEnum):
    Unknown = auto()
    StandardOffer = auto()
    RealtimeLocalLmp = auto()

    @classmethod
    def default(cls) -> "EnergySupplyType":
        return cls.Unknown

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]
