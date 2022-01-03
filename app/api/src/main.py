#!/usr/bin/env python3

import os
import requests
import json 

from geopy.geocoders import Nominatim
from fastapi import FastAPI

#Create an instance of the FastAPI
app = FastAPI()
api_key = os.getenv('API_KEY')
units = "metric"

# Send user location to open weather and return the weather based on location
@app.get("/location/{latitude}/{longitude}")
def getweather( latitude: float, longitude: float ):

    # Geopy to convert out longitude and latitude and an address and then select the city from that address
    engine = Nominatim(user_agent="google")
    # Search our location based on longitude and latitude
    location = engine.reverse(f"{latitude}, {longitude}")
    # Convert out location string in to a list in order to select the address element
    address = location.address.split(",")
    city = address[-6]


    # Request to open weather with our city name and unit to grab back all weather conditions for that city
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}")
    # Convert our responce to a JSON object
    response_json = json.loads(response.text)
    # Filter the JSON object to the temperature 
    temperature = response_json["main"]["temp"]

    return {"temperature" : temperature}


# API health endpoint
@app.get("/health")
def health():
    return {"Health": "Green"}