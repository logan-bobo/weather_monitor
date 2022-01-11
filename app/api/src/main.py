#!/usr/bin/env python3

"""
Instantiate FastAPI along with functions to convert latitude and longitude to temperature
"""

import os
from functools import lru_cache
import requests

from geopy.geocoders import Nominatim
from fastapi import FastAPI

# Create an instance of the FastAPI
APP = FastAPI()
# Set our main api key
API_KEY = os.environ.get('API_KEY')
UNITS = "metric"
# Create an instance of our engine to convert longitude and latitude to an address
ENGINE = Nominatim(user_agent="google")

@lru_cache(maxsize=None)
def get_address(latitude: float, longitude: float):
    """ Return a city name based on latitude and longitude"""

    # Search our location based on longitude and latitude
    location = ENGINE.reverse(f"{latitude}, {longitude}")

    # Get the raw output from out location lookup and select the keys that give us the city name
    address = location.raw["address"]["city"]

    return address

def get_temperature(city: str):
    """ Get the temperature for a city based"""
    # Request to open weather with our city name and unit to grab back all weather
    # conditions for that city
    response = requests.get("https://api.openweathermap.org/data/2.5/weather",
                            params={
                                'q' : city,
                                'appid' : API_KEY,
                                'units' : UNITS,
                            })

    # Set the response JSON to be the json output of the request
    response_json = response.json()

    # Filter the JSON object to the temperature
    temperature = response_json["main"]["temp"]

    return temperature

# Send user location to open weather and return the weather based on location
@APP.get("/location/{latitude}/{longitude}")
def getweather(latitude: float, longitude: float):
    """ Returns a temperature based on a latitude and longitude """
    city = get_address(latitude, longitude)
    temperature = get_temperature(city)

    return {"temperature" : temperature}

# API health endpoint
@APP.get("/health")
def health():
    """ Returns the health of the API"""
    return {"Health": "Green"}
