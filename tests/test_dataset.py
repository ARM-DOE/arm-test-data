import pathlib

from act_test_data import DATASETS, locate


def test_registry():
    files = DATASETS.registry_files
    assert len(files) > 0


def test_locate():
    p = locate()
    assert 'act-test-data-data' in p
    assert pathlib.Path(p)
