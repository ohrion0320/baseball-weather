import requests
import json
import os

with open(os.path.join(os.path.dirname(__file__), "../config.json")) as f:
    config = json.load(f)
    
OPENWEATHER_API_KEY = config["OPENWEATHER_API_KEY"]

def get_weather_by_coords(lat, lon):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat" : lat,
        "lon" : lon,
        "appid" : OPENWEATHER_API_KEY,
        "units" : "metric",
        "lang" : "kr"
    }
    
    try:
        res = requests.get(url, params=params)
    
        if res.status_code == 200:
            return res.json()
    
        else:
            print(f"❌ 요청 실패: {res.status_code}, 내용: {res.text}")
            return None
 
    except Exception as e:
        print(f"⚠️ 예외 발생: {e}")
        return None       
