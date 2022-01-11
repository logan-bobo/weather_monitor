#!/usr/bin/env python3

import os
import requests
import json

from requests import api 

from geopy.geocoders import Nominatim
from fastapi import FastAPI

#Create an instance of the FastAPI
app = FastAPI()
api_key = os.getenv('API_KEY')
units = "metric"
# Geopy to convert out longitude and latitude and an address and then select the city from that address
engine = Nominatim(user_agent="google")

def get_address( latitude: float, longitude: float):
    """ Return a city name based on latitude and longitude"""

    # Search our location based on longitude and latitude
    location = engine.reverse(f"{latitude}, {longitude}")
    # Convert out location string in to a list in order to select the address element
    address = location.address.split(",")
    print(address)

    return address[-6]

def get_temperature(city):
    """ Get the temperature for a city based"""
    # Request to open weather with our city name and unit to grab back all weather conditions for that city
    print(api_key)
    response = requests.get("https://api.openweathermap.org/data/2.5/weather",
        params = {
            'q' : city,
            'appid' : api_key,
            'units' : units,
        }
    )
    print(response.url)
    # Convert our responce to a JSON object
    response_json = json.loads(response.text)
    print(response_json)

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