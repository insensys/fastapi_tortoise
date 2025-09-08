from fastapi import FastAPI
from src.config.app_config import db_settings
from contextlib import asynccontextmanager
from src.config.db_config import TORTOISE_ORM
from tortoise.contrib.fastapi import RegisterTortoise


#TODO: FIrst lets connect one db

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with RegisterTortoise(
        app = app,
        config = TORTOISE_ORM,
    ):
        yield


@app.get("/hello")
async def first_router():
    return "Hello world"