# act-test-data
[![CI](https://github.com/ARM-DOE/act-test-data/actions/workflows/ci.yaml/badge.svg)](https://github.com/ARM-DOE/act-test-data/actions/workflows/ci.yaml)
[![PyPI Version](https://img.shields.io/pypi/v/act-test-data.svg)](https://pypi.python.org/pypi/act-test-data)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/act-test-data.svg)](https://anaconda.org/conda-forge/act-test-data)

A place to share radar data with the community, shared between the open radar packages

## Sample data sets

These files are used as sample data in openradar examples/notebooks and are downloaded by `open-radar-data` package:

- `sample_file`

## Adding new datasets

To add a new dataset file, please follow these steps:

1. Add the dataset file to the `data/` directory
2. From the command line, run `python make_registry.py` script to update the registry file residing in `open_radar_data/registry.txt`
3. Commit and push your changes to GitHub

## Using datasets in notebooks and/or scripts

- Ensure the `act-test-data` package is installed in your environment

  ```bash
  python -m pip install act-test-data

  # or

  python -m pip install git+https://github.com/ARM-DOE/act-test-data

  # or

  conda install -c conda-forge act-test-data
  ```

- Import `DATASETS` and inspect the registry to find out which datasets are available

  ```python
  In [1]: from act_test_data import DATASETS

  In [2]: DATASETS.registry_files
  Out[2]: ['sample_file.nc`]
  ```

- To fetch a data file of interest, use the `.fetch` method and provide the filename of the data file. This will

  - download and cache the file if it doesn't exist already.
  - retrieve and return the local path

  ```python
  In [4]: filepath = DATASETS.fetch('sample_data.nc')

  In [5]: filepath
  Out[5]: '/Users/mgrover/Library/Caches/act-test-data/sample_sgp_data.nc'
  ```

- Once you have access to the local filepath, you can then use it to load your dataset into pandas or xarray or your package of choice:

  ```python
  In [6]: radar = pyart.io.read(filepath)
  ```

## Changing the default data cache location

The default cache location (where the data are saved on your local system) is dependent on the operating system. You can use the `locate()` method to identify it:

```python
from act_test_data import locate
locate()
```

The location can be overwritten by the `ACT_TEST_DATA_DIR` environment
variable to the desired destination.
