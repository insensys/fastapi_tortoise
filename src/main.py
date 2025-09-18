from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.config.db_config import TORTOISE_ORM
from tortoise.contrib.fastapi import RegisterTortoise
from src.schemas.user_create_in import UserCreateIn
from src.models.app_user import AppUser
from fastapi.exceptions import HTTPException
from tortoise import Tortoise
import logging
from src.routers.crud_router import crud_router
from src.routers.invoice_router import invoice_router


@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    await Tortoise.init(config=TORTOISE_ORM)
    yield
    await Tortoise.close_connections()

app = FastAPI(
    title="Tortoise Via FastAPI",
    lifespan=lifespan_handler
)

app.include_router(crud_router)
app.include_router(invoice_router)
