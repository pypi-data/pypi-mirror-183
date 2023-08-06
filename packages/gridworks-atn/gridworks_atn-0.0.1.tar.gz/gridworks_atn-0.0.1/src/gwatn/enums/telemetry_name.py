from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class TelemetryName(StrEnum):
    Unknown = auto()
    PowerW = auto()
    PhaseAngleDegreesTimes10 = auto()
    WattHours = auto()
    RelayState = auto()
    WaterTempCTimes1000 = auto()
    WaterTempFTimes1000 = auto()
    WaterFlowGpmTimes100 = auto()
    CurrentRmsMicroAmps = auto()
    GallonsPerMinuteTimes10 = auto()
    CurrentRmsMilliAmps = auto()
    VoltageRmsMilliVolts = auto()

    @classmethod
    def default(cls) -> "TelemetryName":
        return cls.Unknown

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]
