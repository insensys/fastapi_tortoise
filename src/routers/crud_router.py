from fastapi import APIRouter, Response
from src.schemas.user_create_in import UserCreateIn
from src.db_queries.user_query_crud import create_user as create_user_query


crud_router = APIRouter(
    tags=["CRUD"]
)

@crud_router.post("/create_new_user/")
async def create_user(user_data: UserCreateIn):
    return await create_user_query(user_data)