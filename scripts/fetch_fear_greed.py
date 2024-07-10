import requests
import pandas as pd
from datetime import datetime, timedelta

def fetch_fear_greed():
    url = "https://api.alternative.me/fng/?limit=365"
    response = requests.get(url)
    data = response.json()['data']
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df['value'] = df['value'].astype(int)
    df.rename(columns={'value': 'fear_greed'}, inplace=True)
    df = df[['timestamp', 'fear_greed']]
    df.to_csv('data/fear_greed.csv', index=False)
    return df

if __name__ == "__main__":
    df = fetch_fear_greed()
    print(df.head())
    print(f"Total records fetched: {len(df)}")