import pytest
from xlsxopera import Notebook

file = "test.xlsx"


@pytest.fixture()
def test_file():
    return file


@pytest.fixture()
def tests_book():
    return Notebook(file, "tests")


@pytest.fixture()
def rows_and_cols_book():
    return Notebook("test.xlsx", "rows and cols")


@pytest.fixture()
def data_convert_book():
    return Notebook("test.xlsx", "data convert")
