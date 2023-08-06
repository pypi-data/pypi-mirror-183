"""Type atn.params.report.heatpumpwithbooststore, version 000"""
import json
from typing import Any
from typing import Dict
from typing import Literal
from typing import Optional

from gridworks.errors import SchemaError
from pydantic import BaseModel
from pydantic import validator

from gwatn import property_format
from gwatn.property_format import predicate_validator
from gwatn.schemata.atn_params_heatpumpwithbooststore import (
    AtnParamsHeatpumpwithbooststore,
)
from gwatn.schemata.atn_params_heatpumpwithbooststore import (
    AtnParamsHeatpumpwithbooststore_Maker,
)


class AtnParamsReportHeatpumpwithbooststore(BaseModel):
    GNodeAlias: str  #
    GNodeInstanceId: str  #
    TimeUnixS: int  #
    IrlTimeUnixS: Optional[int] = None
    AtnParams: AtnParamsHeatpumpwithbooststore  #
    TypeName: Literal[
        "atn.params.report.heatpumpwithbooststore"
    ] = "atn.params.report.heatpumpwithbooststore"
    Version: str = "000"

    _validator_g_node_alias = predicate_validator(
        "GNodeAlias", property_format.is_lrd_alias_format
    )

    _validator_g_node_instance_id = predicate_validator(
        "GNodeInstanceId", property_format.is_uuid_canonical_textual
    )

    _validator_time_unix_s = predicate_validator(
        "TimeUnixS", property_format.is_reasonable_unix_time_s
    )

    @validator("IrlTimeUnixS")
    def _validator_irl_time_unix_s(cls, v: Optional[int]) -> Optional[int]:
        if v is None:
            return v
        if not property_format.is_reasonable_unix_time_s(v):
            raise ValueError(f"IrlTimeUnixS {v} must have ReasonableUnixTimeS")
        return v

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        if d["IrlTimeUnixS"] is None:
            del d["IrlTimeUnixS"]
        d["AtnParams"] = self.AtnParams.as_dict()
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class AtnParamsReportHeatpumpwithbooststore_Maker:
    type_name = "atn.params.report.heatpumpwithbooststore"
    version = "000"

    def __init__(
        self,
        g_node_alias: str,
        g_node_instance_id: str,
        time_unix_s: int,
        irl_time_unix_s: Optional[int],
        atn_params: AtnParamsHeatpumpwithbooststore,
    ):
        self.tuple = AtnParamsReportHeatpumpwithbooststore(
            GNodeAlias=g_node_alias,
            GNodeInstanceId=g_node_instance_id,
            TimeUnixS=time_unix_s,
            IrlTimeUnixS=irl_time_unix_s,
            AtnParams=atn_params,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: AtnParamsReportHeatpumpwithbooststore) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> AtnParamsReportHeatpumpwithbooststore:
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> AtnParamsReportHeatpumpwithbooststore:
        d2 = dict(d)
        if "GNodeAlias" not in d2.keys():
            raise SchemaError(f"dict {d2} missing GNodeAlias")
        if "GNodeInstanceId" not in d2.keys():
            raise SchemaError(f"dict {d2} missing GNodeInstanceId")
        if "TimeUnixS" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TimeUnixS")
        if "IrlTimeUnixS" not in d2.keys():
            d2["IrlTimeUnixS"] = None
        if "AtnParams" not in d2.keys():
            raise SchemaError(f"dict {d2} missing AtnParams")
        if not isinstance(d2["AtnParams"], dict):
            raise SchemaError(
                f"d['AtnParams'] {d2['AtnParams']} must be a AtnParamsHeatpumpwithbooststore!"
            )
        atn_params = AtnParamsHeatpumpwithbooststore_Maker.dict_to_tuple(
            d2["AtnParams"]
        )
        d2["AtnParams"] = atn_params
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return AtnParamsReportHeatpumpwithbooststore(
            GNodeAlias=d2["GNodeAlias"],
            GNodeInstanceId=d2["GNodeInstanceId"],
            TimeUnixS=d2["TimeUnixS"],
            IrlTimeUnixS=d2["IrlTimeUnixS"],
            AtnParams=d2["AtnParams"],
            TypeName=d2["TypeName"],
            Version="000",
        )
