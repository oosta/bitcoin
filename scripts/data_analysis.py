import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import BitcoinPrice  # Import the BitcoinPrice model

def load_data():
    engine = create_engine('sqlite:///../data/bitcoin.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(BitcoinPrice).all()
    data = [(row.timestamp, row.price) for row in results]
    df = pd.DataFrame(data, columns=['timestamp', 'price'])
    df.set_index('timestamp', inplace=True)
    session.close()
    return df

def calculate_metrics(df):
    df['daily_return'] = df['price'].pct_change()
    df['volatility'] = df['daily_return'].rolling(window=7).std() * (365 ** 0.5)  # Annualized volatility
    return df

def plot_price(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['price'], label='Bitcoin Price')
    plt.xlabel('Date')
    plt.ylabel('Price (CAD)')
    plt.title('Bitcoin Price Over Time')
    plt.legend()
    plt.show(block=False)

def plot_returns(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['daily_return'], label='Daily Returns')
    plt.xlabel('Date')
    plt.ylabel('Daily Return')
    plt.title('Bitcoin Daily Returns Over Time')
    plt.legend()
    plt.show(block=False)

def plot_volatility(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['volatility'], label='Volatility')
    plt.xlabel('Date')
    plt.ylabel('Volatility (Annualized)')
    plt.title('Bitcoin Volatility Over Time')
    plt.legend()
    plt.show(block=False)

if __name__ == "__main__":
    df = load_data()
    df = calculate_metrics(df)
    plot_price(df)
    plot_returns(df)
    plot_volatility(df)
    plt.show()  # Keeps all figures open
