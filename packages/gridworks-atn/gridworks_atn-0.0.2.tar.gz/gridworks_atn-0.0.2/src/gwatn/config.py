"""Settings for an AtomicTNode, readable from environment and/or from env files."""

import pendulum
from gridworks.gw_config import GNodeSettings


DEFAULT_ENV_FILE = ".env"


class Settings(GNodeSettings):
    g_node_alias: str = "d1.isone.ver.keene.holly"
    g_node_role_value: str = "AtomicTNode"
    my_super_alias: str = "d1.isone.ver.keene.super1"

    market_maker_alias = "d1.isone.ver.keene"
    market_maker_algo_address = (
        "JMEUH2AXM6UGRJO2DBZXDOA2OMIWQFNQZ54LCVC4GQX6QDOX5Z6JRGMWFA"
    )
    mm_api_root = "http://localhost:7997"
    initial_time_unix_s = pendulum.datetime(
        year=2020, month=1, day=1, hour=4, minute=20
    ).int_timestamp

    class Config:
        env_prefix = "ATN_"
        env_nested_delimiter = "__"


class SupervisorSettings(GNodeSettings):
    g_node_alias: str = "d1.isone.ver.keene.super1"
    g_node_role_value: str = "Supervisor"

    class Config:
        env_prefix = "SUPER_"
        env_nested_delimiter = "__"
