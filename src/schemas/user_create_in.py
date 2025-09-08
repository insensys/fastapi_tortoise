from pydantic import BaseModel


class UserCreateIn(BaseModel):
    user_inn: str
    email: str
    password: str
    user_name: str
