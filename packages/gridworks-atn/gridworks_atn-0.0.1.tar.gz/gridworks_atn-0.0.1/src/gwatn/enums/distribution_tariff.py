from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class DistributionTariff(StrEnum):
    Unknown = auto()
    VersantStorageHeatTariff = auto()
    VersantATariff = auto()

    @classmethod
    def default(cls) -> "DistributionTariff":
        return cls.Unknown

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]
