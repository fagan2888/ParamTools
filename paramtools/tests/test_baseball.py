import os

import pytest

from paramtools import parameters

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))


@pytest.fixture
def field_map():
    # nothing here for now
    return {}


@pytest.fixture
def schema_def_path():
    return os.path.join(CURRENT_PATH, "../examples/baseball/schema.json")


@pytest.fixture
def defaults_spec_path():
    return os.path.join(CURRENT_PATH, "../examples/baseball/defaults.json")


@pytest.fixture
def BaseballParams(schema_def_path, defaults_spec_path):
    class _BaseballParams(parameters.Parameters):
        schema = schema_def_path
        defaults = defaults_spec_path

    return _BaseballParams


def test_load_schema(BaseballParams):
    params = BaseballParams()
    assert params
