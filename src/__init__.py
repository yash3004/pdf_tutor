import dataclasses
import os

import dacite
import yaml


@dataclasses.dataclass
class Qdrant:
    host: str
    port: int
    collection_name: str

    def get_client(self):
        return

class MysqlDB:
    host:str
    port:int
    database_name : str


@dataclasses.dataclass
class Configurations:
    openai_api_key: str
    qdrant:Qdrant
    mysql_db:MysqlDB


_cached_config = None


def load_config():
    global _cached_config
    config_file = os.getenv("CONFIG_FILE_PATH", "config.yaml")
    with open(config_file, "rb") as cfg_file:
        cfg = yaml.safe_load(cfg_file)
        _cached_config = dacite.from_dict(data_class=Configurations, data=cfg)
        return _cached_config

