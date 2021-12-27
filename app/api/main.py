#Import API libraties
from fastapi import FastAPI

#Create an instance of the FastAPI
app = FastAPI()

# Send user location to open weather and return the weather based on location
@app.get("/location/{coordinates}")
async def getweather( coordinates: int ):
    return {"location": coordinates}

# API health endpoint
@app.get("/health")
async def health():
    return {"Health": "Green"}