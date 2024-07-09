import sqlite3
import pandas as pd

def load_from_db():
    conn = sqlite3.connect('data/bitcoin.db')
    df = pd.read_sql('SELECT * FROM bitcoin', conn)
    conn.close()
    return df

if __name__ == "__main__":
    df = load_from_db()
    print("Data loaded from database:")
    print(df.head())
    print(f"Total records: {len(df)}")