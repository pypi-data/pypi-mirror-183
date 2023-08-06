from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class MakeModel(StrEnum):
    FREEDOM__RELAY = auto()
    OMEGAEZO__FTB800FLO = auto()
    UNKNOWNMAKE__UNKNOWNMODEL = auto()
    GRIDWORKS__SIMBOOL30AMPRELAY = auto()
    MAGNELAB__SCT0300050 = auto()
    YMDC__SCT013100 = auto()
    G1__NCD_ADS1115__TEWA_NTC_10K_A = auto()
    G1__NCD_ADS1115__AMPH_NTC_10K_A = auto()
    GRIDWORKS__SIMPM1 = auto()
    GRIDWORKS__WATERTEMPHIGHPRECISION = auto()
    NCD__PR814SPST = auto()
    ADAFRUIT__642 = auto()
    SCHNEIDERELECTRIC__IEM3455 = auto()
    OPENENERGY__EMONPI = auto()
    EGAUGE__3010 = auto()
    RHEEM__XE50T10H45U0 = auto()

    @classmethod
    def default(cls) -> "MakeModel":
        return cls.UNKNOWNMAKE__UNKNOWNMODEL

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]
