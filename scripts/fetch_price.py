import pandas as pd
import requests

def fetch_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        "vs_currency": "cad",
        "days": "365",
        "interval": "daily"
    }
    response = requests.get(url, params=params)
    data = response.json()
    prices = data['prices']
    df = pd.DataFrame(prices, columns=['timestamp', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.to_csv('data/bitcoin_prices.csv', index=False)
    return df

if __name__ == "__main__":
    df = fetch_bitcoin_price()
    print(df.head())
    print(f"Total records fetched: {len(df)}")