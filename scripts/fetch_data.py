import pandas as pd

def fetch_data():
    df_prices = pd.read_csv('data/bitcoin_prices.csv', parse_dates=['timestamp'])
    df_fear_greed = pd.read_csv('data/fear_greed.csv', parse_dates=['timestamp'])
    df_volume = pd.read_csv('data/bitcoin_volume.csv', parse_dates=['timestamp'])
    df_trends = pd.read_csv('data/google_trends.csv', parse_dates=['timestamp'])

    df = pd.merge(df_prices, df_fear_greed, on='timestamp', how='outer')
    df = pd.merge(df, df_volume, on='timestamp', how='outer')
    df = pd.merge(df, df_trends, on='timestamp', how='outer')

    # Fill missing values forward and backward
    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)

    df.to_csv('data/bitcoin_data.csv', index=False)
    return df

if __name__ == "__main__":
    df = fetch_data()
    print("Combined Data:")
    print(df.head())
    print(f"Total records: {len(df)}")