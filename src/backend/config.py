from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)
import os

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME_TODO: str
    DB_NAME_POSTGRES: str

    REDIS_HOST: str
    REDIS_PORT: int

    USER_MANAGER_SECRET_KEY: str
    JWT_SECRET_KEY: str

    @property
    def get_asyncpg_dsn_todo(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME_TODO}"

    @property
    def get_asyncpg_dsn(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME_POSTGRES}"

    model_config = SettingsConfigDict(env_file=os.path.join(os.path.dirname(__file__), '.env'))


settings = Settings()
