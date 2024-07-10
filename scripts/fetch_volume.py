import pandas as pd
import requests

def fetch_bitcoin_volume():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        "vs_currency": "cad",
        "days": "365",
        "interval": "daily"
    }
    response = requests.get(url, params=params)
    data = response.json()
    volumes = data['total_volumes']
    df = pd.DataFrame(volumes, columns=['timestamp', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.to_csv('data/bitcoin_volume.csv', index=False)
    return df

if __name__ == "__main__":
    df = fetch_bitcoin_volume()
    print(df.head())
    print(f"Total records fetched: {len(df)}")
