import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather_data(city):
    api_key = os.getenv("API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

import pandas as pd

def process_weather_data(raw_data):
    processed = {
        'city': raw_data['name'],
        'temp': raw_data['main']['temp'],
        'humidity': raw_data['main']['humidity'],
        'timestamp': pd.to_datetime('now')
    }
    return pd.DataFrame([processed])
