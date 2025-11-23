from pydantic_settings import BaseSettings
from pydantic import AnyUrl


class Settings(BaseSettings):
    APP_NAME: str = "Jewellery Store API"
    ENV: str = "development"

    #DB
    DATABASE_URL: AnyUrl = "sqlite+aiosqlite:///./jewellery_store.db"

    class Config:
        env_file = ".env"


settings = Settings()