# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['python_pack_script']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.22.0,<0.23.0']

entry_points = \
{'console_scripts': ['python-pack-script = python_pack_script:main',
                     'python_pack_script = python_pack_script:main']}

setup_kwargs = {
    'name': 'python-pack-script',
    'version': '0.0.6',
    'description': 'Demo RPM builder for python packages',
    'long_description': "# rpm-python-pack\n\nDemo RPM builder for python packages\n\nClone repo\n\n```bash\ngit clone https://github.com/mbrav/rpm-python-pack.git && \\\ncd rpm-python-pack/\n\n```\n\n## Build Python RPM package with setup.py\n\n1. **Install rpm package tools**\n\n    ```bash\n    sudo dnf install -y rpmdevtools rpmlint\n    ```\n\n2. **Build with Python's standard rpm build tool**\n\n    ```bash\n    python setup.py bdist --formats=rpm\n    ```\n\n    <details><summary>ℹ️ Convert pyproject.toml to setup.py</summary>\n    <p>\n\n    ```bash\n    pip3 install poetry2setup --user && \\\n    poetry2setup > setup.py\n    ```\n\n    </p>\n    </details>\n\n    <details><summary>ℹ️ Build RPM package on a non-RHEL distro</summary>\n    <p>\n\n    ```bash\n    sudo apt install rpm && \\\n    python setup.py bdist --formats=rpm\n    ```\n\n    </p>\n    </details>\n\n3. **Install package:**\n\n    ```bash\n    sudo dnf localinstall dist/python-pack-script-*.noarch.rpm\n    ```\n\n4. **Check package info**\n\n    ```bash\n    rpm -qi python-pack-script && which python-pack-script\n    ```\n\n    <details><summary>✅ You should see info about package like so:</summary>\n    <p>\n\n    ```\n    Name        : python-pack-script\n    Version     : 0.0.6\n    Release     : 1\n    Architecture: noarch\n    Install Date: Wed 27 Apr 2022 09:15:34 AM UTC\n    Group       : Development/Libraries\n    Size        : 1155\n    License     : UNKNOWN\n    Signature   : (none)\n    Source RPM  : python-pack-script-0.0.6-1.src.rpm\n    Build Date  : Wed 27 Apr 2022 09:11:18 AM UTC\n    Build Host  : rocky.local\n    Relocations : /usr\n    Vendor      : mbrav <mbrav@protonmail.com>\n    Summary     : Demo RPM builder for python packages\n    Description :\n    UNKNOWN\n    ```\n\n    </p>\n    </details>\n\n5. **Run package**\n\n    ```bash\n    python-pack-script --help\n    ```\n\n    <details><summary>✅ You should see output:</summary>\n    <p>\n\n    This is python-pack-script v0.0.6!\n\n    </p>\n    </details>\n\n</p>\n</details>\n\n<details><summary>✏️ Notes</summary>\n<p>\n\nSetup rpmbuild folder\n\n```bash\nrpmdev-setuptree\n```\n\nIt will create the following folder in your home directory:\n\n```\nrpmbuild/\n├── BUILD\n├── RPMS\n├── SOURCES\n├── SPECS\n└── SRPMS\n```\n\nBuild spec:\n\n```bash\nrpmbuild -ba ./build/bdist.linux-x86_64/rpm/SPECS/python-pack-script.spec\n```\n\n</p>\n</details>\n\n## Build Python package with Poetry (WIP)\n\nThis uses the new [PEP 518](https://peps.python.org/pep-0518/) pyproject.yml standard, but a standard process for building rpm packages seems to yet be established\n\n1. **Install [poetry](https://python-poetry.org/docs/)**\n\n2. **Build Python package**\n\n    ```bash\n    poetry build\n    ```\n\n    <details><summary>ℹ️ Install package with pip</summary>\n    <p>\n\n    Create a new python environment and activate it\n\n    ```bash\n    python3 -m venv venv && source venv/bin/activate\n\n    ```\n\n    Install script into environment\n\n    ```bash\n    pip3 install --no-cache-dir --force-reinstall \\\n    dist/python_pack_script-*-py3-none-any.whl\n    ```\n\n3. **Run script**\n\n    ```bash\n    python -m python_pack_script --help\n    ```\n\n    ✅ You should see a print in your terminal\n\n## Prerequisites for rpm build\n\n-   [_How to create a Linux RPM package_](https://www.redhat.com/sysadmin/create-rpm-package) by Valentin Bajrami (Red Hat)\n-   [_Packaging a Python Wheel as RPM_](https://grimoire.carcano.ch/blog/packaging-a-python-wheel-as-rpm/) by Marco Antonio Carcano\n",
    'author': 'mbrav',
    'author_email': 'mbrav@protonmail.com',
    'maintainer': 'mbrav',
    'maintainer_email': 'mbrav@protonmail.com',
    'url': 'https://github.com/mbrav',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>3.7',
}


setup(**setup_kwargs)

