from fastapi.exceptions import HTTPException
from src.schemas.user_create_in import UserCreateIn
from src.models.app_user import AppUser
import logging
from tortoise import connections


async def validate_unique_user(user_data: UserCreateIn) -> None:
    existing_user = await AppUser.filter(user_inn=user_data.user_inn).first()
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Пользователь с таким ИНН уже существует"
        )

    existing_email = await AppUser.filter(email=user_data.email).first()
    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Пользователь с таким email уже существует"
        )


async def create_user_record(user_data: UserCreateIn) -> AppUser:
    return await AppUser.create(
        user_inn=user_data.user_inn,
        email=user_data.email,
        password=user_data.password,
        user_name=user_data.user_name
    )


def build_user_payload(user: AppUser) -> dict:
    return {
        "success": True,
        "message": "Пользователь успешно создан",
        "user_created": {
            "user_inn": user.user_inn,
            "email": user.email,
            "password": user.password,
            "user_name": user.user_name
        }
    }


async def create_user(user_data: UserCreateIn) -> dict:
    replica_conn = connections.get("replica")
    try:
        await validate_unique_user(user_data)
        new_user = await create_user_record(user_data)
        # await AppUser.create(user_data,using_db=connections.get("replica"))
        # await AppUser.using_db(connections.get("replica")).create(user_data)
        sec_db_user = await AppUser.create(
            user_inn = user_data.user_inn,
            email = user_data.email,
            password = user_data.password,
            user_name =user_data.user_name,
            using_db= replica_conn
        )
        return build_user_payload(new_user)
    except HTTPException:
        raise
    except Exception as e:
        logging.error("Error creating user", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Ошибка создания пользователя: {repr(e)}"
        )