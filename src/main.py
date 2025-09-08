from fastapi import FastAPI
from src.config.app_config import db_settings
from contextlib import asynccontextmanager
from src.config.db_config import TORTOISE_ORM
from tortoise.contrib.fastapi import RegisterTortoise
from src.schemas.user_create_in import UserCreateIn
from src.models.app_user import AppUser
from fastapi.exceptions import HTTPException
from tortoise import Tortoise
import logging


@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    await Tortoise.init(config=TORTOISE_ORM)

    yield

    await Tortoise.close_connections()

app = FastAPI(
    title="Tortoise Via FastAPI",
    lifespan=lifespan_handler
)



@app.post("/create-user")
async def create_user(user_data: UserCreateIn):

    try:
        existing_user = await AppUser.filter(user_inn = user_data.user_inn).first()
        if existing_user:
            raise HTTPException(
                status_code=400,
                detail = f"Пользователь с таким ИНН уже существует"
            )
        
        existing_email = await AppUser.filter(email = user_data.email).first()
        if existing_email:
            raise HTTPException(
                status_code=400,
                detail="Пользователь с таким email уже существует"
            )
        
        new_user = await AppUser.create(
            user_inn = user_data.user_inn,
            email = user_data.email,
            password = user_data.password,
            user_name = user_data.user_name
        )

        return {
            "success": True,
            "message": "Пользователь успешно создан",
            "user_created": {
                "user_inn": new_user.user_inn,
                "email": new_user.email,
                "password": new_user.password,
                "user_name": new_user.user_name
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        logging.error("Error creating user:", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Ошибка создания пользователя: {repr(e)}"
        )
    