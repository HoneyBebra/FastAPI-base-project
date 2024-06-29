import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME: str = os.getenv('APP_NAME', 'Service')
    APP_DESCRIPTION: str = os.getenv('APP_DESCRIPTION', 'Description')
    APP_VERSION: str = os.getenv('APP_VERSION', '0.0.1')

    API_V1_PREFIX: str = os.getenv('API_V1_PREFIX', '/api/v1')
    APP_PORT: int = int(os.getenv('APP_PORT', '8000'))

    LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'info')
