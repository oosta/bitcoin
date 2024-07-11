import pandas as pd
import requests

def fetch_usd_to_cad_exchange_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data['rates']['CAD']

def fetch_bitcoin_price():
    url = "https://api.binance.com/api/v3/klines"
    params = {
        "symbol": "BTCUSDT",
        "interval": "1d",
        "limit": 730  # Fetch data for the last 730 days (2 years)
    }
    response = requests.get(url, params=params)
    data = response.json()

    if isinstance(data, list):
        prices = [[item[0], item[4]] for item in data]  # Use the opening timestamp and closing price
        df = pd.DataFrame(prices, columns=['timestamp', 'price'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        
        exchange_rate = fetch_usd_to_cad_exchange_rate()
        df['price'] = df['price'].astype(float) * exchange_rate  # Convert to CAD
        
        df.to_csv('data/bitcoin_prices.csv', index=False)
        return df
    else:
        print("Error: Data format is incorrect or 'prices' key not found in the API response.")
        print(data)  # Debugging: Print the entire response to check its structure
        return pd.DataFrame()  # Return an empty DataFrame if 'prices' key is missing

if __name__ == "__main__":
    df = fetch_bitcoin_price()
    if not df.empty:
        print(df.head())
        print(f"Total records fetched: {len(df)}")
    else:
        print("No data fetched due to missing 'prices' key in the response.")
