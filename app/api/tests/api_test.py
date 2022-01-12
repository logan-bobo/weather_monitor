#!/usr/bin/env python3

import unittest
from unittest.mock import Mock

from src.main import health, getweather, get_address, get_temperature

mock = Mock()

class TestAPI(unittest.TestCase):

    
    def test_health(self):
        health_output = health()
        assert health_output == {"Health": "Green"}

    @mock.patch('get_address.address', return_value="testcity")
    def test_address(self):
        address_value = get_address(123/123)
        assert address_value == "testcity"

    @mock.patch("get_temperature.temperature", return_value=0)
    def test_temperature(self):
        temperature = get_temperature()
        assert temperature == 0

    def test_location(self):
        weather = getweather(53.480837, -2.244914)
        assert 0 <= weather["temperature"] <= 100

if __name__ == 'main':
    unittest.main()