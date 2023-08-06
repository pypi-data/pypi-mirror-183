"""
Define the object lists / table view for each of the plugin models.
"""

import django_tables2 as tables
from netbox.tables import NetBoxTable, columns

from .models.disk import DataDisk

__all__ = (
    "DataDiskTable",
)


class DataDiskTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    parent = tables.Column(
        linkify=True,
        order_by=('virtual_machine')
    )

    class Meta(NetBoxTable.Meta):
        model = DataDisk
        fields = (
            'virtual_machine', 'size', 'vg_name', 'lv_name', 'mount_path'
        )
        default_columns = ('virtual_machine', 'size', 'vg_name', 'lv_name', 'mount_path')
