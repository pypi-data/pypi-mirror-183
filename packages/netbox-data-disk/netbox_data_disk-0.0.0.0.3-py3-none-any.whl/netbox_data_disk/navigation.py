"""
Define the plugin menu buttons & the plugin navigation bar enteries.
"""

from extras.plugins import PluginMenuButton, PluginMenuItem

#
# Define plugin menu buttons
#


menu_items = (
    PluginMenuItem(
        link="plugins:netbox_data_disk:datadisk_list",
        link_text="Data Disks",
    )
)