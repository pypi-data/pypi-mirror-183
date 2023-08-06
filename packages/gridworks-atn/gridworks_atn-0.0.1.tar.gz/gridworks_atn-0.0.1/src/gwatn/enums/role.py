from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class Role(StrEnum):
    PrimaryScada = auto()
    HomeAlone = auto()
    Heatpump = auto()
    MultipurposeSensor = auto()
    CurrentTransformer = auto()
    RadiatorFan = auto()
    PipeFlowMeter = auto()
    BaseboardRadiator = auto()
    CirculatorPump = auto()
    DedicatedThermalStore = auto()
    HeatedSpace = auto()
    HydronicPipe = auto()
    PrimaryMeter = auto()
    Outdoors = auto()
    BoostElement = auto()
    BooleanActuator = auto()
    Atn = auto()
    TankWaterTempSensor = auto()
    PipeTempSensor = auto()
    RoomTempSensor = auto()
    OutdoorTempSensor = auto()

    @classmethod
    def default(cls) -> "Role":
        return cls.HeatedSpace

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]
