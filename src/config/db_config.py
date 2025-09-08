from tortoise.contrib.fastapi import RegisterTortoise
from src.config.app_config import db_settings
from contextlib import asynccontextmanager
from src.main import FastAPI


TORTOISE_ORM = {
    "connections":{"default": db_settings.get_async_db_url},
    "apps": {
        "models":{
            "models":["src.models"],
            "default_connection": "default",
        },
    },
}

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with RegisterTortoise(
        app = app,
        config = TORTOISE_ORM,
    ):
        yield
