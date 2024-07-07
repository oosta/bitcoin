import requests
import pandas as pd
import time

def fetch_bitcoin_data():
    # Fetch data for the last year (365 days)
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        "vs_currency": "usd",  # Change to "cad" if you want prices in CAD
        "days": "365"  # Number of days for this chunk
    }
    
    for attempt in range(3):  # Retry up to 3 times
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise HTTPError for bad responses
            data = response.json()
            
            if 'prices' in data:
                prices = data['prices']
                df = pd.DataFrame(prices, columns=['timestamp', 'price'])
                df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
                return df
            else:
                print(f"No 'prices' key in response.")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}. Retrying...")
            time.sleep(5)  # Wait for 5 seconds before retrying
    
    raise ValueError("Failed to fetch data from the API.")

if __name__ == "__main__":
    try:
        df = fetch_bitcoin_data()
        print(df.head())
        print(f"Total records fetched: {len(df)}")
    except ValueError as e:
        print(e)
