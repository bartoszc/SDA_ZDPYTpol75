import pytest


@pytest.fixture
def test_data():
    data = [1, 2, 3, 4, 5]
    return data


def test_data_sum(test_data):
    result = sum(test_data)
    assert result == 15


def test_data_contains_element(test_data):
    assert 3 in test_data