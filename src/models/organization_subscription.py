from tortoise import fields
from tortoise.models import Model


class OrganizationSubscription(Model):
    id = fields.IntField(pk=True)
    organization_tin = fields.ForeignKeyField(
        model_name="models.Organization",
        related_name= "organizations",
    )
    subscription_name = fields.ForeignKeyField(
        "models.Subscription",
        related_name="subscription")
    is_active = fields.BooleanField(null=False)

    class Meta:
        table = "organization_subscription"


"""
experimental=# \d organization_subscription
                                         Table "public.organization_subscription"
      Column       |          Type          | Collation | Nullable |                        Default

-------------------+------------------------+-----------+----------+---------------------------------------------
----------
 id                | integer                |           | not null | nextval('organization_subscription_id_seq'::
regclass)
 organization_tin  | character varying(255) |           | not null |
 subscription_name | character varying(150) |           | not null |
 is_active         | boolean                |           | not null |
Indexes:
    "organization_subscription_pkey" PRIMARY KEY, btree (id)
Foreign-key constraints:
    "organization_subscription_organization_tin_fkey" FOREIGN KEY (organization_tin) REFERENCES organization(lega
l_person_tin)
    "organization_subscription_subscription_name_fkey" FOREIGN KEY (subscription_name) REFERENCES subscription(na
me)
"""