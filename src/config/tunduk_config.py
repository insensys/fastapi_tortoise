from pydantic_settings import BaseSettings, SettingsConfigDict


class TundukConfig(BaseSettings):
    GNS_TOKEN:str
    USER_TIN:str
    TUNDUK_URL:str
    X_ROAD_CLIENT:str
    CLIENT_UUID:str

    @property
    def get_gns_token(self) -> str:
        return(self.GNS_TOKEN)

    @property
    def get_user_tin(self) -> str:
        return(self.USER_TIN)

    @property
    def get_tunduk_url(self) -> str:
        return(self.TUNDUK_URL)

    @property
    def get_x_road_client(self) -> str:
        return(self.X_ROAD_CLIENT)

    @property
    def get_client_uuid(self):
        return(self.CLIENT_UUID)

    model_config = SettingsConfigDict(
        env_file=(".env"),
        extra="allow"
    )

tunduk_configs=TundukConfig()