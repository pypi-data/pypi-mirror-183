from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class MixingValveFeedbackModel(StrEnum):
    ConstantSwt = auto()
    NaiveVariableSwt = auto()
    CautiousVariableSwt = auto()

    @classmethod
    def default(cls) -> "MixingValveFeedbackModel":
        return cls.ConstantSwt

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]
