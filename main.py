import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from geofence import determine_state

load_dotenv()

app = FastAPI()

# Hardcoded coords for testing
HOME_LAT = 40.0083
HOME_LON = -105.2698

class LocationPayload(BaseModel):
    latitude: float
    longitude: float

@app.post("/location")
async def update_location(payload: LocationPayload):
    current_state = determine_state(
        phone_lat=payload.latitude, 
        phone_lon=payload.longitude,
        home_lat=HOME_LAT,
        home_lon=HOME_LON
    )
    
    print(f"Calculated State: {current_state.upper()}")
    
    return {"status": "success", "calculated_state": current_state}