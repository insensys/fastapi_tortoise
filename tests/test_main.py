import pytest
from src.main import create_user
from src.schemas.user_create_in import UserCreateIn


@pytest.mark.asyncio
async def test_create_user():
    test_user_data = UserCreateIn(
        user_name="test_user",
        password="test_password",
        user_inn="test_123",
        email="test@mail.io"
                      )
    
    result = await create_user(test_user_data)
    assert result is not None
    assert result.username=="test_user"