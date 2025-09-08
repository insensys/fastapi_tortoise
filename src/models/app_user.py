from tortoise import fields
from tortoise.models import Model


class AppUser(Model):
    user_inn = fields.CharField(max_length=50, pk=True)
    email = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=255)
    user_name = fields.CharField(max_length=35)
    created_at = fields.DatetimeField(auto_now_add=True)

    organizations: fields.ReverseRelation["Organization"]

    class Meta:
        table = "app_user"
