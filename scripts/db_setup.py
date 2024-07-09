import sqlite3
import pandas as pd

def save_to_db(df):
    conn = sqlite3.connect('data/bitcoin.db')
    df.to_sql('bitcoin', conn, if_exists='replace', index=False)
    conn.close()

if __name__ == "__main__":
    df = pd.read_csv('data/bitcoin_data.csv')
    save_to_db(df)
    print("Data saved to database successfully.")