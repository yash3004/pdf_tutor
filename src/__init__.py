import dataclasses
import logging
import os

import yaml
from dacite import from_dict
from qdrant_client import QdrantClient
from pymongo import MongoClient
from qdrant_client.http.models import VectorParams, Distance

_logger = logging.getLogger()


@dataclasses.dataclass
class Qdrant:
    host: str
    port: int
    collection_name: str
    _client: QdrantClient

    def get_client(self):
        self._client = QdrantClient(host=self.host, port=self.port)

    def get_collection(self):
        collection = self._client.get_collection(collection_name=self.collection_name)
        if collection is None:
            collection = self._client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(size=100, distance=Distance.COSINE),
            )
        return collection


class Mongo:
    host: str
    port: int
    db_name: str
    _client: MongoClient

    def get_client(self):
        self._client = MongoClient(host=self.host, port=self.port)

    def get_database(self):
        self._client.get_database(name=self.db_name)


@dataclasses.dataclass
class Configurations:
    openai_api_key: str
    qdrant: Qdrant
    mongo: Mongo

    def qdrant_collection(self):
        self.qdrant.get_client()
        return self.qdrant.get_collection()

    def mongo_db(self):
        self.mongo.get_client()
        return self.mongo.get_database()


_cached_config = None


def load_config() -> Configurations:
    global _cached_config
    if _cached_config is not None:
        return _cached_config

    config_path = os.environ.get("CONFIG_LOCATION", "config.yaml")
    _logger.info(f"reading from config file")

    with open(config_path, "r") as cfg:
        config = yaml.safe_load(cfg)

        print(config)

    _cached_config = from_dict(data_class=Configurations, data=config)
    return _cached_config
