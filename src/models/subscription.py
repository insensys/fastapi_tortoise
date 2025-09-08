from tortoise import fields
from tortoise.models import Model

class Subscription(Model):
    name = fields.CharField(max_length=50, pk=True)
    description = fields.TextField(null=False)

    organizations: fields.ReverseRelation["OrganizationSubscription"]

    class Meta:
        table = "subscription"