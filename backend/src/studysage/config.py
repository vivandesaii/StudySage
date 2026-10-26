from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# Find the backend/ directory automatically (3 levels up from src/studysage/config.py)
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


class Settings(BaseSettings):
    database_url: str
    db_echo_sql: bool = False

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
