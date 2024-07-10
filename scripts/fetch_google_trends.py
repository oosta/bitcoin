from pytrends.request import TrendReq
import pandas as pd
from datetime import datetime, timedelta
import time

def fetch_google_trends():
    pytrends = TrendReq(hl='en-US', tz=360)
    kw_list = ["Bitcoin"]
    
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    timeframe = f"{start_date.strftime('%Y-%m-%d')} {end_date.strftime('%Y-%m-%d')}"
    
    pytrends.build_payload(kw_list, cat=0, timeframe=timeframe, geo='', gprop='')

    while True:
        try:
            trends_data = pytrends.interest_over_time()
            if 'isPartial' in trends_data.columns:
                trends_data = trends_data.drop(columns=['isPartial'])
            break
        except Exception as e:
            print(f"Error: {e}. Retrying in 60 seconds...")
            time.sleep(60)
    
    trends_data.reset_index(inplace=True)
    trends_data.rename(columns={'date': 'timestamp', 'Bitcoin': 'google_trends'}, inplace=True)
    trends_data.to_csv('data/google_trends.csv', index=False)
    return trends_data

if __name__ == "__main__":
    df_trends = fetch_google_trends()
    print(df_trends.head())
    print(f"Total records fetched: {len(df_trends)}")
