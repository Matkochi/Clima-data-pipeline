from extract import get_weather_data
from transform import process_weather_data
from load import save_to_db

def main():
    cities = ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]
    for city in cities:
        raw_data = get_weather_data(city)
        processed_data = process_weather_data(raw_data)
        save_to_db(processed_data)
    print("Pipeline executado com sucesso!")

if __name__ == "__main__":
    main()
