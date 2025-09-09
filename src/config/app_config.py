from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    HOST:str 
    PORT:str 
    USER:str 
    PASSWORD:str
    DB_NAME:str
    DB_NAME2:str

    @property
    def get_async_db_url(self) -> str:
        return (
            f"asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DB_NAME}"
            )

    @property
    def get_async_db_url2(self) ->str:
        return(
            f"asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DB_NAME2}"
        )

    model_config = SettingsConfigDict(
        env_file=(".env"),
        extra="allow"
    )


db_settings = DBSettings()
