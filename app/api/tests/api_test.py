#!/usr/bin/env python3

import pytest

from src.main import health, getweather

# Test for our health endpoint
def test_health():
    health_output = health()
    assert health_output == {"Health": "Green"}

# Test for our locations
def test_location():
    weather = getweather(53.480837, -2.244914)
    assert 0 <= weather["temperature"] <= 100