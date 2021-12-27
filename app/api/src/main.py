#!/usr/bin/env python3

#Import API libraties
from fastapi import FastAPI

#Create an instance of the FastAPI
app = FastAPI()

# Send user location to open weather and return the weather based on location
@app.get("/location/{coordinates}")
def getweather( coordinates: int ):
    return {"location": coordinates}

# API health endpoint
@app.get("/health")
def health():
    return {"Health": "Green"}