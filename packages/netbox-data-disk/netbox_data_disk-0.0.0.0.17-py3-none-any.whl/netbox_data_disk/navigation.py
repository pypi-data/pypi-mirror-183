from extras.plugins import PluginMenuButton, PluginMenuItem
from extras.plugins import PluginMenu
from utilities.choices import ButtonColorChoices

view_menu_item = PluginMenuItem(
    link="plugins:netbox_data_disk:view_list",
    link_text="Views",
    permissions=["netbox_data_disk.view_view"],
    buttons=(
        PluginMenuButton(
            "plugins:netbox_data_disk:view_add",
            "Add",
            "mdi mdi-plus-thick",
            ButtonColorChoices.GREEN,
            permissions=["netbox_data_disk.add_view"],
        ),
        PluginMenuButton(
            "plugins:netbox_data_disk:view_import",
            "Import",
            "mdi mdi-upload",
            ButtonColorChoices.CYAN,
            permissions=["netbox_data_disk.add_view"],
        ),
    ),
)

zone_menu_item = PluginMenuItem(
    link="plugins:netbox_data_disk:zone_list",
    link_text="Zones",
    permissions=["netbox_data_disk.view_zone"],
    buttons=(
        PluginMenuButton(
            "plugins:netbox_data_disk:zone_add",
            "Add",
            "mdi mdi-plus-thick",
            ButtonColorChoices.GREEN,
            permissions=["netbox_data_disk.add_zone"],
        ),
        PluginMenuButton(
            "plugins:netbox_data_disk:zone_import",
            "Import",
            "mdi mdi-upload",
            ButtonColorChoices.CYAN,
            permissions=["netbox_data_disk.add_zone"],
        ),
    ),
)

nameserver_menu_item = PluginMenuItem(
    link="plugins:netbox_data_disk:nameserver_list",
    link_text="Nameservers",
    permissions=["netbox_data_disk.view_nameserver"],
    buttons=(
        PluginMenuButton(
            "plugins:netbox_data_disk:nameserver_add",
            "Add",
            "mdi mdi-plus-thick",
            ButtonColorChoices.GREEN,
            permissions=["netbox_data_disk.add_nameserver"],
        ),
        PluginMenuButton(
            "plugins:netbox_data_disk:nameserver_import",
            "Import",
            "mdi mdi-upload",
            ButtonColorChoices.CYAN,
            permissions=["netbox_data_disk.add_nameserver"],
        ),
    ),
)

record_menu_item = PluginMenuItem(
    link="plugins:netbox_data_disk:record_list",
    link_text="Records",
    permissions=["netbox_data_disk.view_record"],
    buttons=(
        PluginMenuButton(
            "plugins:netbox_data_disk:record_add",
            "Add",
            "mdi mdi-plus-thick",
            ButtonColorChoices.GREEN,
            permissions=["netbox_data_disk.add_record"],
        ),
        PluginMenuButton(
            "plugins:netbox_data_disk:record_import",
            "Import",
            "mdi mdi-upload",
            ButtonColorChoices.CYAN,
            permissions=["netbox_data_disk.add_record"],
        ),
    ),
)

managed_record_menu_item = PluginMenuItem(
    link="plugins:netbox_data_disk:managed_record_list",
    link_text="Managed Records",
    permissions=["netbox_data_disk.view_record"],
)

menu = PluginMenu(
    label="NetBox DNS",
    groups=(
        (
            "DNS Configuration",
            (
                view_menu_item,
                zone_menu_item,
                nameserver_menu_item,
                record_menu_item,
                managed_record_menu_item,
            ),
        ),
    ),
    icon_class="mdi mdi-dns",
)
