from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/weather/{city}")
async def get_weather(city: str):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    async with httpx.AsyncClient() as client:
        geo_res = await client.get(url)
        geo_data = geo_res.json()
    if not geo_data.get("results"):
        return {"error": "City not found"}

    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    async with httpx.AsyncClient() as client:
        weather_res = await client.get(weather_url)
    return weather_res.json()

@app.get("/crypto/{symbol}")
async def get_crypto_price(symbol: str):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    async with httpx.AsyncClient() as client:
        res = await client.get(url)
    return res.json()

@app.get("/github-trending")
async def get_trending_repos():
    url = "https://ghapi.huchen.dev/repositories"
    async with httpx.AsyncClient() as client:
        res = await client.get(url)
    return res.json()
