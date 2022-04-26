# rpm-python-pack

Test RPM package builder for python package

### Build Python package

Install [poetry](https://python-poetry.org/docs/)

Clone repo

```bash
git clone https://github.com/mbrav/rpm-python-pack.git && \
cd rpm-python-pack/

```

Build Python package

```bash
poetry build
```

<details><summary>ℹ️ Install package with pip</summary>
<p>

Create a new python environment and activate it

```bash
python -m venv venv && source venv/bin/activate

```

Install script into environment

```bash
pip3 install --no-cache-dir --force-reinstall dist/python_pack_script-*-py3-none-any.whl
```

Run script

```bash
python -m python_pack_script
```

✅ You should see a print in your terminal

</p>
</details>

### Prerequisites for rpm build

-   [Source](https://www.redhat.com/sysadmin/create-rpm-package)
