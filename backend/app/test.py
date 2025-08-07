import json
from weather import get_weather_by_coords

with open("backend/app/data/stadiums.json", "r", encoding="utf-8") as f:
    stadiums = json.load(f)

for stadium in stadiums:
    name = stadium["name"]
    lat = stadium["lat"]
    lon = stadium["lon"]

    print(f"\n🏟️ {name} 날씨 조회 중...")
    weather = get_weather_by_coords(lat, lon)

    if weather:
        print(f"✅ {name} 날씨: {weather['weather'][0]['description']}, {weather['main']['temp']}°C")
    else:
        print(f"❌ {name} 날씨 정보를 가져올 수 없습니다.")
