# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['python_pack_script']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['python-pack-script = python_pack_script.main:script']}

setup_kwargs = {
    'name': 'python-pack-script',
    'version': '0.0.4',
    'description': 'Demo RPM builder for python packages',
    'long_description': None,
    'author': 'mbrav',
    'author_email': 'mbrav@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>3.7',
}


setup(**setup_kwargs)

