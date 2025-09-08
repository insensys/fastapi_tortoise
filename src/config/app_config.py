from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    HOST: str
    PORT: str
    USER: str
    PASSWORD: str
    DB_NAME: str

    model_config = SettingsConfigDict(
        env_file=(".env"),
        extra="ignore"
    )

    @property
    def get_async_db_url(self) -> str:
        return f"asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DB_NAME}"

db_settings = DBSettings()

"""
asyncpg: asyncpg://postgres:pass@db.host:5432/somedb
"""