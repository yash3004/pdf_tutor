import dataclasses


@dataclasses.dataclass
class Qdrant:
    host: str
    port: str
    collection_name: str

    def get_client(self):
        return


@dataclasses.dataclass
class Configurations:
    openai_api_key: str


def load_config():
    return 0
