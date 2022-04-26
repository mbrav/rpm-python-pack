# rpm-python-pack

Test RPM package builder for python package

Clone repo

```bash
git clone https://github.com/mbrav/rpm-python-pack.git && \
cd rpm-python-pack/

```

## Build Python RPM package with setup.py

1. Install rpm package tools

    ```bash
    sudo dnf install -y rpmdevtools rpmlint
    ```

<!--2. Setup rpmbuild folder

    ```bash
    rpmdev-setuptree
    ```

    It will create the following folder in your home directory:

    ```
    rpmbuild/
    ├── BUILD
    ├── RPMS
    ├── SOURCES
    ├── SPECS
    └── SRPMS
    ``` -->

2. Build with Python's standard rpm build tool:

    ```bash
    python3 setup.py bdist_rpm
    ```

<!-- 3. Build spec:

    ```bash
    rpmbuild -ba ./build/bdist.linux-x86_64/rpm/SPECS/python_pack_script.spec
    ``` -->

3. Install package:

    ```bash
    sudo dnf localinstall dist/python_pack_script-*-1.noarch.rpm
    ```

4. ✅ Check package info:

    ```bash
    dnf info python_pack_script
    ```

## Build Python package with Poetry (WIP)

This uses the new [PEP 518](https://peps.python.org/pep-0518/) pyproject.yml standard, but a standard process for building rpm packages seems to yet be established

1. Install [poetry](https://python-poetry.org/docs/)

2. Build Python package

    ```bash
    poetry build
    ```

    <details><summary>ℹ️ Install package with pip</summary>
    <p>

    Create a new python environment and activate it

    ```bash
    python3 -m venv venv && source venv/bin/activate

    ```

    Install script into environment

    ```bash
    pip3 install --no-cache-dir --force-reinstall dist/python_pack_script-*-py3-none-any.whl
    ```

    Run script

    ```bash
    python3 -m python_pack_script
    ```

    ✅ You should see a print in your terminal

    </p>
    </details>

## Prerequisites for rpm build

-   [_How to create a Linux RPM package_](https://www.redhat.com/sysadmin/create-rpm-package) by Valentin Bajrami (Red Hat)
-   [_Packaging a Python Wheel as RPM_](https://grimoire.carcano.ch/blog/packaging-a-python-wheel-as-rpm/) by Marco Antonio Carcano
