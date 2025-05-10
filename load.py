import sqlite3
import os

def save_to_db(df):
    db_path = os.getenv("DB_PATH", "data/weather.db")
    conn = sqlite3.connect(db_path)
    df.to_sql('weather', conn, if_exists='append', index=False)
    conn.close()
