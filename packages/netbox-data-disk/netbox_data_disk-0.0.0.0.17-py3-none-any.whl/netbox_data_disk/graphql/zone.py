from graphene import ObjectType

from netbox.graphql.fields import ObjectField, ObjectListField
from netbox.graphql.types import NetBoxObjectType

from netbox_data_disk.models import Zone
from netbox_data_disk.filters import ZoneFilter


class ZoneType(NetBoxObjectType):
    class Meta:
        model = Zone
        fields = "__all__"
        filterset_class = ZoneFilter


class ZoneQuery(ObjectType):
    zone = ObjectField(ZoneType)
    zone_list = ObjectListField(ZoneType)
