#!/usr/bin/env python3

import pytest
from unittest.mock import Mock

from src.main import health, getweather, get_address, get_temperature

mock = Mock()

# Test for our health endpoint
def test_health():
    health_output = health()
    assert health_output == {"Health": "Green"}

@mock.patch('get_address.address', return_value="testcity")
def test_address():
    address_value = get_address()
    assert address_value == "testcity"

@mock.patch("get_temperature.temperature", return_value=0)
def test_temperature():
    temperature = get_temperature()
    assert temperature == 0

# Test for our locations
def test_location():
    weather = getweather(53.480837, -2.244914)
    assert 0 <= weather["temperature"] <= 100