<h1 align="center">Data Science Manager 👨‍💻</h1>
<p>
  <a href="#" target="_blank">
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.13-blue.svg?cacheSeconds=2592000" />
  </a>
  <a href="#" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-pdoc-orange.svg" />
  </a>
  <a href="LICENSE" target="_blank">
    <img alt="License: Adel Rayane Amrouche" src="https://img.shields.io/badge/License-Adel Rayane Amrouche-yellow.svg" />
  </a>
</p>

> Data Science tools to ease access and use of data and models

## Install

The easiest way to install scikit-learn is using `pip`:
```sh
pip install dsmanager
```
or `poetry`
```sh
poetry add dsmanager
```
or `conda`
```sh
conda install dsmanager
```

Multiple sub dependencies are available depending on the needs:
```sh
pip install dsmanager[sharepoint] # Add Sharepoint source handling
pip install dsmanager[salesforce] # Add SalesForce source handling
pip install dsmanager[kaggle] # Add Kaggle source handling
pip install dsmanager[snowflake] # Add Snowflkae source handling
pip install dsmanager[mysql] # Add MySQL source handling
pip install dsmanager[pgsql] # Add PostgreSQL source handling
```

## Usage

The DS Manager has 3 main components:
- A **DataManager** component
- A **Controller** component
- A **Model** component

### DataManager

The DataManager allows to manage different types of data sources among which we can mention:
- Local (local and online files)
- Http (Http requests)
- Ftp (Ftp hosted files)
- Sql (Sql database tables)
- Sharepoint (Microsoft OneDrive files)
- SalesForce (SalesForce classes)
- Kaggle (Kaggle datasets)


```python
from dsmanager import DataManager
dm = DataManager("data/metadata.json")
```

## Development

### Source code

You can check the latest sources with the command:

```python
git clone https://gitlab.com/bigrayou/dsmanager
```

### Source code

After installation, you can launch the test suite from outside the dsmanager directory (you will need to have pytest >= 5.3.1 installed):
```python
pytest -v
```

### Dependencies

The DSManager requires:
 - dash >=2.7.1,<3.0.0
 - explainerdashboard >=0.4.0,<0.5.0
 - llvmlite >=0.39.1,<0.40.0
 - numba >=0.56.4,<0.57.0
 - numexpr >=2.8.4,<3.0.0
 - numpy >=1.23.3,<2.0.0
 - openpyxl >=3.0.10,<4.0.0
 - pandas >=1.5.0,<2.0.0
 - pickle-mixin >=1.0.2,<2.0.0
 - python-dotenv >=0.21.0,<0.22.0
 - requests >=2.28.1,<3.0.0
 - scikit-learn >=1.2.0,<2.0.0
 - setuptools >=65.6.3,<66.0.0
 - sqlalchemy >=1.4.45,<2.0.0
 - sweetviz >=2.1.4,<3.0.0
 - tqdm >=4.64.1,<5.0.0

Optionnaly, the DSManager could require:
 - azure-common >=1.1.28,<2.0.0
 - azure-storage-blob >=12.14.1,<13.0.0
 - azure-storage-common >=2.1.0,<3.0.0
 - kaggle >=1.5.12,<2.0.0
 - shareplum >=0.5.1,<0.6.0
 - simple-salesforce >=1.12.2,<2.0.0
 - snowflake-sqlalchemy >=1.4.4,<2.0.0
 - psycopg2-binary >=2.9.5,<3.0.0
 - mysqlclient >=2.1.1,<3.0.0

## Author

👤 **Rayane Amrouche**

* Github: [@AARayane](https://github.com/AARayane)
* Gitlab: [@AARayane](https://gitlab.com/bigrayou)
