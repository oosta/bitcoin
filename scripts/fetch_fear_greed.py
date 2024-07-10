import requests
import pandas as pd

def fetch_fear_greed_index():
    url = "https://api.alternative.me/fng/?limit=365"  # Fetch data for the past year
    response = requests.get(url)
    data = response.json()

    values = data['data']
    timestamps = [item['timestamp'] for item in values]
    timestamps = pd.to_datetime(timestamps, unit='s')
    fear_greed_values = [int(item['value']) for item in values]

    df = pd.DataFrame({'timestamp': timestamps, 'fear_greed': fear_greed_values})
    return df

if __name__ == "__main__":
    df = fetch_fear_greed_index()
    print(df.head())
    df.to_csv('data/fear_greed_index.csv', index=False)
    print(f"Total records fetched: {len(df)}")
