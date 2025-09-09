from tortoise.contrib.fastapi import RegisterTortoise
from src.config.app_config import db_settings
from contextlib import asynccontextmanager
from src.main import FastAPI
from tortoise import backends


TORTOISE_ORM = {
    "connections":{"default": db_settings.get_async_db_url, 
                   "replica": db_settings.get_async_db_url2},
    "apps": {
        "models":{
            "models":["src.models"],
            "default_connection": "default",
        },
    },
}

@asynccontextmanager
async def lifespan(app: FastAPI):
    generate_schemas=True
    async with RegisterTortoise(
        app = app,
        config = TORTOISE_ORM,
    ):
        yield
