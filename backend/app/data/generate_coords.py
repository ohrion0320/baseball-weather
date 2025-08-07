import requests
import json
import os

# config.json에서 Kakao API 키 불러오기
with open(os.path.join(os.path.dirname(__file__), "../../config.json")) as f:
    config = json.load(f)

headers = {
    "Authorization": f"KakaoAK {config['KAKAO_API_KEY']}"
}

stadiums = [
    {"name": "잠실종합운동장 잠실야구장", "address": "서울 송파구 올림픽로 25"},
    {"name": "고척스카이돔", "address": "서울 구로구 경인로 430"},
    {"name": "대구삼성라이온즈파크", "address": "대구 수성구 야구전설로 1"},
    {"name": "광주기아챔피언스필드", "address": "광주 북구 서림로 10"},
    {"name": "인천SSG랜더스필드", "address": "인천 미추홀구 매소홀로 618"},
    {"name": "한화생명이글스파크", "address": "대전 중구 대종로 373"},
    {"name": "창원NC파크", "address": "경남 창원시 마산회원구 삼호로 63"},
    {"name": "수원KT위즈파크", "address": "경기 수원시 장안구 경수대로 893"},
    {"name": "부산사직종합운동장 사직야구장", "address": "부산 동래구 사직로 45"}
]

result = []

for stadium in stadiums:
    url = "https://dapi.kakao.com/v2/local/search/address.json"
    params = {"query": stadium["address"]}
    res = requests.get(url, params=params, headers=headers)
    
    print(f"📡 {stadium['name']} 응답코드: {res.status_code}")
    print("📨 응답 내용:", res.json())

    if res.status_code == 200 and res.json()["documents"]:
        coords = res.json()["documents"][0]["address"]
        stadium["lat"] = coords["y"]
        stadium["lon"] = coords["x"]
        result.append(stadium)
    else:
        print(f"⚠️ 주소 변환 실패: {stadium['name']}")

with open("backend/app/data/stadiums.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("✅ stadiums.json 파일 저장 완료!")
