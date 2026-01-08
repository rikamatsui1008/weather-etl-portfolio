import os
import requests
import mysql.connector
from datetime import datetime

API_KEY = os.getenv("OPENWEATHER_API_KEY")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
CITY = "Tokyo"

def fetch_weather():
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": CITY, "appid": API_KEY, "units": "metric"}
    res = requests.get(url, params=params)
    res.raise_for_status()
    return res.json()

def transform_weather(data):
    return {
        "city": data["name"],
        "date_time": datetime.fromtimestamp(data["dt"]),
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["main"]
    }

def load_to_mysql(w):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=MYSQL_PASSWORD,
        database="weather_db"
    )
    cursor = conn.cursor()
    sql = """
    INSERT INTO weather (city, date_time, temp, humidity, weather)
    VALUES (%s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE temp=%s, humidity=%s, weather=%s
    """
    values = (
        w["city"], w["date_time"], w["temp"], w["humidity"], w["weather"],
        w["temp"], w["humidity"], w["weather"]
    )
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    data = fetch_weather()
    weather = transform_weather(data)
    load_to_mysql(weather)
