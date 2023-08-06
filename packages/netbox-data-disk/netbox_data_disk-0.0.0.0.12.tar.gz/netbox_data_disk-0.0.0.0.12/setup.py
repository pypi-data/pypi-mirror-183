# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['netbox_data_disk', 'netbox_data_disk.migrations']

package_data = \
{'': ['*'], 'netbox_data_disk': ['templates/netbox_data_disk/*']}

setup_kwargs = {
    'name': 'netbox-data-disk',
    'version': '0.0.0.0.12',
    'description': 'Netbox Disk Plugin',
    'long_description': 'pip3 install poetry\npoetry build\npoetry publish\n\ngit add . && git commit -m "add change to project" && git push\n\npsql --username netbox --password --host localhost netbox\n\n\\dt\n\n\nSELECT table_name, column_name, data_type FROM information_schema.columns WHERE table_name = \'netbox_acls_accesslist\';\n\nSELECT table_name, column_name, data_type FROM information_schema.columns WHERE table_name = \'virtualization_virtualmachine\';\n\n\nvirtualization_virtualmachine;\n\npython manage.py makemigrations netbox_data_disk --dry-run\n\n\nhttp://localhost:8000/plugins/data-disk/data-disk',
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
