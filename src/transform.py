import pandas as pd

def process_weather_data(raw_data):
    processed = {
        'city': raw_data['name'],
        'temp': raw_data['main']['temp'],
        'humidity': raw_data['main']['humidity'],
        'timestamp': pd.to_datetime('now')
    }
    return pd.DataFrame([processed])
