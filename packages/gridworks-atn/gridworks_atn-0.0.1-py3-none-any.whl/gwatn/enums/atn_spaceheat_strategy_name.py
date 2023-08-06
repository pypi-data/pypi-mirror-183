from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class AtnSpaceheatStrategyName(StrEnum):
    NoActor = auto()
    SupervisorA = auto()
    HeatPumpWithBoostStore = auto()

    @classmethod
    def default(cls) -> "AtnSpaceheatStrategyName":
        return cls.NoActor

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]
