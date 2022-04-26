# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['python_pack_script']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'python-pack-script',
    'version': '0.0.3',
    'description': 'Demo RPM builder for python packages',
    'long_description': None,
    'author': 'mbrav',
    'author_email': 'mbrav@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>3.7',
}


setup(**setup_kwargs)

