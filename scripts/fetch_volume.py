import pandas as pd
import requests

def fetch_bitcoin_volume():
    url = "https://api.binance.com/api/v3/klines"
    params = {
        "symbol": "BTCUSDT",
        "interval": "1d",
        "limit": 730  # Fetch data for the last 730 days (2 years)
    }
    response = requests.get(url, params=params)
    data = response.json()

    if isinstance(data, list):
        volumes = [[item[0], item[5]] for item in data]  # Use the opening timestamp and volume
        df = pd.DataFrame(volumes, columns=['timestamp', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.to_csv('data/bitcoin_volume.csv', index=False)
        return df
    else:
        print("Error: Data format is incorrect or 'total_volumes' key not found in the API response.")
        print(data)  # Debugging: Print the entire response to check its structure
        return pd.DataFrame()  # Return an empty DataFrame if 'total_volumes' key is missing

if __name__ == "__main__":
    df = fetch_bitcoin_volume()
    if not df.empty:
        print(df.head())
        print(f"Total records fetched: {len(df)}")
    else:
        print("No data fetched due to missing 'total_volumes' key in the response.")
