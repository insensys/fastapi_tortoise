from tortoise.contrib.fastapi import RegisterTortoise
from src.config.app_config import db_settings

TORTOISE_ORM = {
    "connections":{"default": db_settings.get_async_db_url},
    "apps": {
        "models":{
            "models":["src.models"],
            "default_connection": "default",
        },
    },
    "use_tz": False,
    "timezone": "UTC"
}