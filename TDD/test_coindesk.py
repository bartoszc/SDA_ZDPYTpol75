import json
import pytest
import requests


@pytest.fixture
def crypto_price():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    return response.json()


def test_updated_field_exists(crypto_price):
    assert "updated" in crypto_price["time"]


def test_gbp_rate_greater_than_zero(crypto_price):
    assert crypto_price["bpi"]["GBP"]["rate_float"] > 0

