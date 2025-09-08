from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    HOST:str 
    PORT:str 
    USER:str 
    PASSWORD:str
    DB_NAME:str

    @property
    def get_async_db_url(self) -> str:
        return (
            f"asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DB_NAME}"
            )

    model_config = SettingsConfigDict(
        env_file=(".env"),
        extra="allow"
    )


db_settings = DBSettings()

"""
    HOST=localhost
    PORT=5432
    USER=localhost_user
    PASSWORD:1234
    DB_NAME:experimental

asyncpg: asyncpg://postgres:pass@db.host:5432/somedb
"""