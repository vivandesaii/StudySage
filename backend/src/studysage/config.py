from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# Find the backend/ directory automatically (3 levels up from src/studysage/config.py)
BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    database_url: str
    db_user: str
    db_password: str
    db_name: str

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


settings = Settings()
