#!/usr/bin/env python3

import os
import requests
import json 
import geopy
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
    location = engine.reverse(f"{latitude}, {longitude}")
    address = location.address.split(",")
    city = address[-6]


    # Request to open weather with out city name and unity to grab back all weather conditions for that city
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}")
    response_json = json.loads(response.text)
    temperature = response_json["main"]["temp"]

    return {"temperature" : temperature}


# API health endpoint
@app.get("/health")
def health():
    return {"Health": "Green"}