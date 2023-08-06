# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['netbox_data_disk',
 'netbox_data_disk.management',
 'netbox_data_disk.management.commands',
 'netbox_data_disk.migrations',
 'netbox_data_disk.models',
 'netbox_data_disk.templatetags',
 'netbox_data_disk.utils']

package_data = \
{'': ['*'],
 'netbox_data_disk': ['templates/netbox_data_disk/*',
                      'templates/netbox_data_disk/inc/*']}

setup_kwargs = {
    'name': 'netbox-data-disk',
    'version': '0.0.0.0.15',
    'description': 'Netbox Disk Plugin',
    'long_description': 'pip3 install poetry\npoetry build\npoetry publish\n\ngit add . && git commit -m "add change to project" && git push\n\npsql --username netbox --password --host localhost netbox\n\n\\dt\n\n\nSELECT table_name, column_name, data_type FROM information_schema.columns WHERE table_name = \'netbox_acls_accesslist\';\n\nSELECT table_name, column_name, data_type FROM information_schema.columns WHERE table_name = \'virtualization_virtualmachine\';\n\n\nvirtualization_virtualmachine;\n\npython manage.py makemigrations netbox_data_disk --dry-run\n\n\nhttp://localhost:8000/plugins/data-disk/data-disk\n\n\nhttps://github.com/ryanmerolle/netbox-acls\nhttps://github.com/iDebugAll/nextbox-ui-plugin\nhttps://github.com/PieterL75/netbox_ipcalculator/\nhttps://github.com/hudson-trading/netbox-nagios\n\nhttps://github.com/netbox-community/netbox-plugin-tutorial\nhttps://github.com/netbox-community/netbox',
    'author': 'Tim Rhomberg',
    'author_email': 'timrhomberg@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
