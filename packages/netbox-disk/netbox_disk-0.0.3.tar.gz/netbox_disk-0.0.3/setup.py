# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['netbox_disk', 'netbox_disk.templatetags']

package_data = \
{'': ['*'], 'netbox_disk': ['templates/*']}

setup_kwargs = {
    'name': 'netbox-disk',
    'version': '0.0.3',
    'description': 'Netbox Disk Plugin',
    'long_description': 'pip3 install poetry\npoetry build\npoetry publish',
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
