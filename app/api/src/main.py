#!/usr/bin/env python3

import os
import requests
from requests import api 

from geopy.geocoders import Nominatim
from fastapi import FastAPI

# Create an instance of the FastAPI
app = FastAPI()
# Set our main api key
api_key = os.getenv('API_KEY')
units = "metric"
# Create an instance of our engine to convert longitude and latitude to an address
engine = Nominatim(user_agent="google")

def get_address( latitude: float, longitude: float):
    """ Return a city name based on latitude and longitude"""

    # Search our location based on longitude and latitude
    location = engine.reverse(f"{latitude}, {longitude}")
    # Convert out location string in to a list in order to select the address element
    address = location.address.split(",")

    return address[-6]

def get_temperature(city):
    """ Get the temperature for a city based"""
    # Request to open weather with our city name and unit to grab back all weather conditions for that city
    response = requests.get("https://api.openweathermap.org/data/2.5/weather",
        params = {
            'q' : city,
            'appid' : api_key,
            'units' : units,
        }
    )

    # Set the response JSON to be the json output of the request
    response_json = response.json()
    
    # Filter the JSON object to the temperature 
    return response_json["main"]["temp"]


# Send user location to open weather and return the weather based on location
@app.get("/location/{latitude}/{longitude}")
def getweather( latitude: float, longitude: float ):
    city = get_address(latitude, longitude)
    temperature = get_temperature(city)

    return {"temperature" : temperature}

# API health endpoint
@app.get("/health")
def health():
    return {"Health": "Green"}