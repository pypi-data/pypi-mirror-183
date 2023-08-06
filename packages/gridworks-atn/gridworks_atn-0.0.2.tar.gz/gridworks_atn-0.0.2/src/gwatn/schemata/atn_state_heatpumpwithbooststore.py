"""Type atn.state.heatpumpwithbooststore, version 000"""
import json
from typing import Any
from typing import Dict
from typing import Literal

from gridworks.errors import SchemaError
from pydantic import BaseModel
from pydantic import validator

from gwatn import property_format
from gwatn.property_format import predicate_validator


class AtnStateHeatpumpwithbooststore(BaseModel):
    FromGNodeAlias: str  #
    FromGNodeInstanceId: str  #
    BoostPowerKwTimes1000: int  #
    HeatpumpPowerKwTimes1000: int  #
    StoreKwh: int  #
    CopTimes10: int  #
    MaxStoreKwh: int  #
    AboutTerminalAssetAlias: str  #
    TypeName: Literal[
        "atn.state.heatpumpwithbooststore"
    ] = "atn.state.heatpumpwithbooststore"
    Version: str = "000"

    _validator_from_g_node_alias = predicate_validator(
        "FromGNodeAlias", property_format.is_lrd_alias_format
    )

    _validator_from_g_node_instance_id = predicate_validator(
        "FromGNodeInstanceId", property_format.is_uuid_canonical_textual
    )

    _validator_about_terminal_asset_alias = predicate_validator(
        "AboutTerminalAssetAlias", property_format.is_lrd_alias_format
    )

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class AtnStateHeatpumpwithbooststore_Maker:
    type_name = "atn.state.heatpumpwithbooststore"
    version = "000"

    def __init__(
        self,
        from_g_node_alias: str,
        from_g_node_instance_id: str,
        boost_power_kw_times1000: int,
        heatpump_power_kw_times1000: int,
        store_kwh: int,
        cop_times10: int,
        max_store_kwh: int,
        about_terminal_asset_alias: str,
    ):
        self.tuple = AtnStateHeatpumpwithbooststore(
            FromGNodeAlias=from_g_node_alias,
            FromGNodeInstanceId=from_g_node_instance_id,
            BoostPowerKwTimes1000=boost_power_kw_times1000,
            HeatpumpPowerKwTimes1000=heatpump_power_kw_times1000,
            StoreKwh=store_kwh,
            CopTimes10=cop_times10,
            MaxStoreKwh=max_store_kwh,
            AboutTerminalAssetAlias=about_terminal_asset_alias,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: AtnStateHeatpumpwithbooststore) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> AtnStateHeatpumpwithbooststore:
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> AtnStateHeatpumpwithbooststore:
        d2 = dict(d)
        if "FromGNodeAlias" not in d2.keys():
            raise SchemaError(f"dict {d2} missing FromGNodeAlias")
        if "FromGNodeInstanceId" not in d2.keys():
            raise SchemaError(f"dict {d2} missing FromGNodeInstanceId")
        if "BoostPowerKwTimes1000" not in d2.keys():
            raise SchemaError(f"dict {d2} missing BoostPowerKwTimes1000")
        if "HeatpumpPowerKwTimes1000" not in d2.keys():
            raise SchemaError(f"dict {d2} missing HeatpumpPowerKwTimes1000")
        if "StoreKwh" not in d2.keys():
            raise SchemaError(f"dict {d2} missing StoreKwh")
        if "CopTimes10" not in d2.keys():
            raise SchemaError(f"dict {d2} missing CopTimes10")
        if "MaxStoreKwh" not in d2.keys():
            raise SchemaError(f"dict {d2} missing MaxStoreKwh")
        if "AboutTerminalAssetAlias" not in d2.keys():
            raise SchemaError(f"dict {d2} missing AboutTerminalAssetAlias")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return AtnStateHeatpumpwithbooststore(
            FromGNodeAlias=d2["FromGNodeAlias"],
            FromGNodeInstanceId=d2["FromGNodeInstanceId"],
            BoostPowerKwTimes1000=d2["BoostPowerKwTimes1000"],
            HeatpumpPowerKwTimes1000=d2["HeatpumpPowerKwTimes1000"],
            StoreKwh=d2["StoreKwh"],
            CopTimes10=d2["CopTimes10"],
            MaxStoreKwh=d2["MaxStoreKwh"],
            AboutTerminalAssetAlias=d2["AboutTerminalAssetAlias"],
            TypeName=d2["TypeName"],
            Version="000",
        )
