from fastapi import APIRouter
from weather import get_weather_by_coords
import json
import os

router = APIRouter()

DATA_PATH = os.path.join(os.path.dirname(__file__),"data","stadiums.json")

@router.get("/weather")
def get_all_stadiums_weather():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        stadiums = json.load(f)
    
    result = []
    
    for stadium in stadiums:
        lat = stadium["lat"]
        lon = stadium["lon"]
        name = stadium["name"]

        weather = get_weather_by_coords(lat, lon)

        if weather:
            result.append({
                "name": name,
                "lat": lat,
                "lon": lon,
                "weather": {
                    "description": weather["weather"][0]["description"],
                    "temperature": weather["main"]["temp"]
                }
            })
        else:
            result.append({
                "name": name,
                "lat": lat,
                "lon": lon,
                "weather": None
            })

    return result
