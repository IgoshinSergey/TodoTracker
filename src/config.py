from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME_TODO: str
    DB_NAME_POSTGRES: str

    USER_MANAGER_SECRET_KEY: str
    JWT_SECRET_KEY: str

    @property
    def get_asyncpg_dsn_todo(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME_TODO}"

    @property
    def get_asyncpg_dsn(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}"

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
