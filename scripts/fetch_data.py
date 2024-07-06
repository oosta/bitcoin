import requests
import pandas as pd

def fetch_bitcoin_data():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        "vs_currency": "cad",  
        "days": "30"  # Fetch data for the last 30 days
    }
    response = requests.get(url, params=params)
    data = response.json()
    prices = data['prices']
    df = pd.DataFrame(prices, columns=['timestamp', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

if __name__ == "__main__":
    df = fetch_bitcoin_data()
    print(df.head())
