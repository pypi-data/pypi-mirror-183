from extras.plugins import PluginMenuItem, PluginMenuButton, PluginMenu
from utilities.choices import ButtonColorChoices

item = PluginMenuItem(
        link='plugins:netbox_data_disk:backup_list',
        link_text='Devices',
        buttons=[
            PluginMenuButton(
                link="plugins:netbox_data_disk:backup_add",
                title="Add",
                icon_class="mdi mdi-plus",
                color=ButtonColorChoices.GREEN,
            ),
        ]
    )

menu = PluginMenu(
        label="Configuration Backup",
        groups=(
            ('Backup Jobs', (item,)),
        )
    )
