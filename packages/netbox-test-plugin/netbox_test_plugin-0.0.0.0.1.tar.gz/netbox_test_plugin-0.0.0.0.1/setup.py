# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['netbox_data_disk',
 'netbox_data_disk.api',
 'netbox_data_disk.fields',
 'netbox_data_disk.filters',
 'netbox_data_disk.forms',
 'netbox_data_disk.graphql',
 'netbox_data_disk.management.commands',
 'netbox_data_disk.migrations',
 'netbox_data_disk.tables',
 'netbox_data_disk.templatetags',
 'netbox_data_disk.tests',
 'netbox_data_disk.tests.nameserver',
 'netbox_data_disk.tests.record',
 'netbox_data_disk.tests.view',
 'netbox_data_disk.tests.zone',
 'netbox_data_disk.views']

package_data = \
{'': ['*'],
 'netbox_data_disk': ['templates/netbox_data_disk/*',
                      'templates/netbox_data_disk/record/*',
                      'templates/netbox_data_disk/zone/*']}

setup_kwargs = {
    'name': 'netbox-test-plugin',
    'version': '0.0.0.0.1',
    'description': 'Netbox Test Plugin',
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
