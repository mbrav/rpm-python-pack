# rpm-python-pack

Demo RPM builder for python packages

Clone repo

```bash
git clone https://github.com/mbrav/rpm-python-pack.git && \
cd rpm-python-pack/

```

## Build Python RPM package with setup.py

1. **Install rpm package tools**

    ```bash
    sudo dnf install -y rpmdevtools rpmlint
    ```

2. **Build with Python's standard rpm build tool**

    ```bash
    python setup.py bdist --formats=rpm
    ```

    <details><summary>ℹ️ Convert pyproject.toml to setup.py</summary>
    <p>

    ```bash
    pip3 install poetry2setup --user && \
    poetry2setup > setup.py
    ```

    </p>
    </details>

    <details><summary>ℹ️ Build RPM package on a non-RHEL distro</summary>
    <p>

    ```bash
    sudo apt install rpm && \
    python setup.py bdist --formats=rpm
    ```

    </p>
    </details>

3. **Install package:**

    ```bash
    sudo dnf localinstall dist/python-pack-script-*.noarch.rpm
    ```

4. **Check package info**

    ```bash
    rpm -qi python-pack-script && which python-pack-script
    ```

    <details><summary>✅ You should see info about package like so:</summary>
    <p>

    ```
    Name        : python-pack-script
    Version     : 0.0.5
    Release     : 1
    Architecture: noarch
    Install Date: Wed 27 Apr 2022 09:15:34 AM UTC
    Group       : Development/Libraries
    Size        : 1155
    License     : UNKNOWN
    Signature   : (none)
    Source RPM  : python-pack-script-0.0.5-1.src.rpm
    Build Date  : Wed 27 Apr 2022 09:11:18 AM UTC
    Build Host  : rocky.local
    Relocations : /usr
    Vendor      : mbrav <mbrav@protonmail.com>
    Summary     : Demo RPM builder for python packages
    Description :
    UNKNOWN
    ```

    </p>
    </details>

5. **Run package**

    ```bash
    python-pack-script --help
    ```

    <details><summary>✅ You should see output:</summary>
    <p>

    This is python-pack-script v0.0.5!

    </p>
    </details>

</p>
</details>

<details><summary>✏️ Notes</summary>
<p>

Setup rpmbuild folder

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
```

Build spec:

```bash
rpmbuild -ba ./build/bdist.linux-x86_64/rpm/SPECS/python-pack-script.spec
```

</p>
</details>

## Build Python package with Poetry (WIP)

This uses the new [PEP 518](https://peps.python.org/pep-0518/) pyproject.yml standard, but a standard process for building rpm packages seems to yet be established

1. **Install [poetry](https://python-poetry.org/docs/)**

2. **Build Python package**

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
    pip3 install --no-cache-dir --force-reinstall \
    dist/python_pack_script-*-py3-none-any.whl
    ```

3. **Run script**

    ```bash
    python -m python_pack_script --help
    ```

    ✅ You should see a print in your terminal

## Prerequisites for rpm build

-   [_How to create a Linux RPM package_](https://www.redhat.com/sysadmin/create-rpm-package) by Valentin Bajrami (Red Hat)
-   [_Packaging a Python Wheel as RPM_](https://grimoire.carcano.ch/blog/packaging-a-python-wheel-as-rpm/) by Marco Antonio Carcano
