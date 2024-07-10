import requests
import pandas as pd
from datetime import datetime, timedelta

def fetch_bitcoin_data():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)  # Fetch data for the past year
    url = f'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range'
    params = {
        'vs_currency': 'cad',  # Change to CAD
        'from': int(start_date.timestamp()),
        'to': int(end_date.timestamp())
    }
    response = requests.get(url, params=params)
    data = response.json()

    prices = data['prices']
    timestamps = [datetime.utcfromtimestamp(price[0] / 1000) for price in prices]
    prices = [price[1] for price in prices]

    df = pd.DataFrame({'timestamp': timestamps, 'price': prices})
    return df

def fetch_data():
    df_prices = fetch_bitcoin_data()
    df_fng = pd.read_csv('data/fear_greed_index.csv')
    
    # Ensure both timestamps are in datetime format
    df_prices['timestamp'] = pd.to_datetime(df_prices['timestamp'])
    df_fng['timestamp'] = pd.to_datetime(df_fng['timestamp'])
    
    # Merge the dataframes on timestamp
    df = pd.merge(df_prices, df_fng, on='timestamp', how='left')
    df.to_csv('data/bitcoin_data.csv', index=False)
    return df

if __name__ == "__main__":
    df = fetch_data()
    print(df.head())
    print(f"Total records fetched: {len(df)}")
