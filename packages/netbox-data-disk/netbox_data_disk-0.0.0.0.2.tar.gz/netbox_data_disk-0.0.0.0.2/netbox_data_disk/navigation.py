"""
Define the plugin menu buttons & the plugin navigation bar enteries.
"""

from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

#
# Define plugin menu buttons
#

datadisk_buttons = [
    PluginMenuButton(
        link="plugins:netbox_data_disk:datadisk_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
        color=ButtonColorChoices.GREEN,
    )
]

#
# Define navigation bar links including the above buttons defined.
#

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_data_disk:datadisk_list",
        link_text="Data Disks",
        buttons=datadisk_buttons,
    )
)
