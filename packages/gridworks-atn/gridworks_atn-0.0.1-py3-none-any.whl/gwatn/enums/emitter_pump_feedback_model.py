from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class EmitterPumpFeedbackModel(StrEnum):
    ConstantDeltaT = auto()
    ConstantGpm = auto()

    @classmethod
    def default(cls) -> "EmitterPumpFeedbackModel":
        return cls.ConstantDeltaT

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]
