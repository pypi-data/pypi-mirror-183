"""
Define the NetBox Plugin
"""

from extras.plugins import PluginConfig


class NetBoxDataDiskConfig(PluginConfig):
    name = "netbox_data_disk"
    verbose_name = "Data Disk"
    description = "Manage data disks"
    version = "0.0.0.0.2"
    base_url = "data-disk"


config = NetBoxDataDiskConfig
