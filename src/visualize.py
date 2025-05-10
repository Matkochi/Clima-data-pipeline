# visualize.py
import matplotlib.pyplot as plt
import sqlite3

def generate_plot(db_path):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql("SELECT * FROM weather", conn)
    df.plot(x='city', y='temp', kind='bar')
    plt.savefig('output/temp_plot.png')
