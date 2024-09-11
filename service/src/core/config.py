from functools import lru_cache
from logging import config as logging_config
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.core.logger import LOGGING

load_dotenv()

BASE_DIR = Path(__file__).parent.parent.parent
ENV_FILE = BASE_DIR / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_FILE)

    app_name: str = "Service"
    app_description: str = "Description"
    app_version: str = "0.0.1"

    app_port: int = 8000

    log_level: str = "INFO"

    # These parameters also need to be changed in the nginx and docker settings
    api_v1_prefix: str = "/api/v1"


@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore[call-arg]


settings = get_settings()

logging_config.dictConfig(LOGGING)
