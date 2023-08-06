""" List of all the types used"""
from typing import Dict
from typing import List
from typing import no_type_check

from gwatn.schemata import AcceptedBid_Maker
from gwatn.schemata import AtnBid_Maker
from gwatn.schemata import AtnParamsHeatpumpwithbooststore_Maker
from gwatn.schemata import AtnParamsReportHeatpumpwithbooststore_Maker
from gwatn.schemata import AtnStateHeatpumpwithbooststore_Maker
from gwatn.schemata import BidAck_Maker
from gwatn.schemata import FloParamsHeatpumpwithbooststore_Maker
from gwatn.schemata import GNodeGt_Maker
from gwatn.schemata import GNodeInstanceGt_Maker
from gwatn.schemata import HeartbeatA_Maker
from gwatn.schemata import LatestPrice_Maker
from gwatn.schemata import MarketPrice_Maker
from gwatn.schemata import MarketSlot_Maker
from gwatn.schemata import MarketTypeGt_Maker
from gwatn.schemata import PriceQuantity_Maker
from gwatn.schemata import PriceQuantityUnitless_Maker
from gwatn.schemata import Ready_Maker
from gwatn.schemata import SimTimestep_Maker
from gwatn.schemata import SuperStarter_Maker
from gwatn.schemata import SupervisorContainerGt_Maker
from gwatn.schemata import TadeedSpecsHack_Maker
from gwatn.schemata import TerminalassetCertifyHack_Maker


TypeMakerByName: Dict[str, HeartbeatA_Maker] = {}


@no_type_check
def type_makers() -> List[HeartbeatA_Maker]:
    return [
        AcceptedBid_Maker,
        AtnBid_Maker,
        AtnParamsHeatpumpwithbooststore_Maker,
        AtnParamsReportHeatpumpwithbooststore_Maker,
        AtnStateHeatpumpwithbooststore_Maker,
        BidAck_Maker,
        FloParamsHeatpumpwithbooststore_Maker,
        GNodeGt_Maker,
        GNodeInstanceGt_Maker,
        HeartbeatA_Maker,
        LatestPrice_Maker,
        MarketPrice_Maker,
        MarketSlot_Maker,
        MarketTypeGt_Maker,
        PriceQuantity_Maker,
        PriceQuantityUnitless_Maker,
        Ready_Maker,
        SimTimestep_Maker,
        SuperStarter_Maker,
        SupervisorContainerGt_Maker,
        TadeedSpecsHack_Maker,
        TerminalassetCertifyHack_Maker,
    ]


for maker in type_makers():
    TypeMakerByName[maker.type_name] = maker


def version_by_type_name() -> Dict[str, str]:
    """
    Returns:
        Dict[str, str]: Keys are TypeNames, values are versions
    """

    v: Dict[str, str] = {
        "accepted.bid": "000",
        "atn.bid": "000",
        "atn.params.heatpumpwithbooststore": "000",
        "atn.params.report.heatpumpwithbooststore": "000",
        "atn.state.heatpumpwithbooststore": "000",
        "bid.ack": "000",
        "flo.params.heatpumpwithbooststore": "000",
        "g.node.gt": "000",
        "g.node.instance.gt": "000",
        "heartbeat.a": "001",
        "latest.price": "000",
        "market.price": "000",
        "market.slot": "000",
        "market.type.gt": "000",
        "price.quantity": "000",
        "price.quantity.unitless": "000",
        "ready": "001",
        "sim.timestep": "000",
        "super.starter": "000",
        "supervisor.container.gt": "000",
        "tadeed.specs.hack": "000",
        "terminalasset.certify.hack": "000",
    }

    return v


def status_by_versioned_type_name() -> Dict[str, str]:
    """
    Returns:
        Dict[str, str]: Keys are versioned TypeNames, values are type status
    """

    v: Dict[str, str] = {
        "accepted.bid.000": "Pending",
        "atn.bid.000": "Pending",
        "atn.params.heatpumpwithbooststore.000": "Active",
        "atn.params.report.heatpumpwithbooststore.000": "Pending",
        "atn.state.heatpumpwithbooststore.000": "Pending",
        "bid.ack.000": "Pending",
        "flo.params.heatpumpwithbooststore.000": "Active",
        "g.node.gt.000": "Pending",
        "g.node.instance.gt.000": "Pending",
        "heartbeat.a.001": "Pending",
        "latest.price.000": "Pending",
        "market.price.000": "Pending",
        "market.slot.000": "Pending",
        "market.type.gt.000": "Pending",
        "price.quantity.000": "Pending",
        "price.quantity.unitless.000": "Pending",
        "ready.001": "Pending",
        "sim.timestep.000": "Pending",
        "super.starter.000": "Pending",
        "supervisor.container.gt.000": "Pending",
        "tadeed.specs.hack.000": "Pending",
        "terminalasset.certify.hack.000": "Pending",
    }

    return v
