from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Baseball_Stadium_Weather" : "KBO리그 1군 야구장 날씨 확인!!"}