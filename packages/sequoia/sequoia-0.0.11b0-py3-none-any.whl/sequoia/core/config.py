import os
import sys
import toml
from typing import Any
from munch import DefaultMunch
from pydantic import BaseSettings
from functools import lru_cache

current = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))))

sys.path.append(current)
sys.path.append('/home/modules')


def load_toml(settings: BaseSettings) -> Any:
    stage = os.getenv("PROJECT_STAGE") or "dev"
    t = toml.load(f".env.{stage}.toml")
    # t = toml.load(f"{current}/.env.{stage}.toml")

    if "SCHEMA" in t:
        schema = t["SCHEMA"]
    else:
        schema = os.getenv("SCHEMA") or "z_local"
    t["SCHEMA"] = schema
    os.environ["SCHEMA"] = schema
    tt = DefaultMunch.fromDict(t, object())
    return tt


class Config(BaseSettings):
    ENV: str = "local"
    DEBUG: bool = True
    REDIS: Any
    SCHEMA: str = "z_local"
    JWT_SECRET_KEY: str = "RizaMasykurSecretCode007"
    JWT_ALGORITHM: str = "HS256"
    SENTRY_SDN: Any = None
    GCP_PUBSUB: Any
    SLACK: str

    class Config:
        extra = "allow"
        env_file_encoding = "utf-8"

        @classmethod
        def customise_sources(
            cls,
            init_settings,
            env_settings,
            file_secret_settings,
        ):
            return (
                init_settings,
                load_toml,
                env_settings,
                file_secret_settings,
            )


@lru_cache
def get_config():
    return Config()


config: Config = get_config()
