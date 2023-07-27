import pytest
import json


@pytest.fixture
def json_data():
    test_one = "example string"
    with open('user.json') as f:
        data = json.load(f)
    return data


@pytest.mark.skip(reason="Waiting for fixes")
def test_user_name_in_json(json_data):
    assert "name" in json_data


def test_user_data_in_json(json_data):
    assert json_data["name"] == "John"
    assert json_data["age"] == 30
    assert json_data["city"] == "New York"

