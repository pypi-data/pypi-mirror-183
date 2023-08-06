import django_tables2 as tables

from netbox.tables import NetBoxTable, TagColumn

from netbox_data_disk.models import NameServer


class NameServerTable(NetBoxTable):
    """Table for displaying NameServer objects."""

    name = tables.Column(
        linkify=True,
    )
    tags = TagColumn(
        url_name="plugins:netbox_data_disk:nameserver_list",
    )

    class Meta(NetBoxTable.Meta):
        model = NameServer
        fields = (
            "pk",
            "name",
            "description",
            "tags",
        )
        default_columns = (
            "pk",
            "name",
            "tags",
        )
