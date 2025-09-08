from tortoise import fields
from tortoise.models import Model


class Organization(Model):
    legal_person_tin = fields.CharField(max_length=255, pk=True)
    organization_name = fields.CharField(max_length=255)
    user = fields.ForeignKeyField(
        "models.AppUser",
        related_name="organizations",
        to_field="user_inn",
        on_delete=fields.CASCADE,
        null=True
    )

    subscriptions: fields.ReverseRelation["OrganizationSubscription"]

    class Meta:
        table="organization"