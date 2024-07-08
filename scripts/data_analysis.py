import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import BitcoinPrice  # Import the BitcoinPrice model
from trading_signals import get_latest_signal, calculate_trading_signal  # Import trading signal functions
from technical_indicators import calculate_sma, calculate_ema, calculate_rsi, calculate_macd  # Import technical indicators

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
    plt.plot(df.index, df['price'], label='Bitcoin Price', color='blue')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.title('Bitcoin Price Over Time')
    plt.legend()
    plt.grid(True)
    plt.show(block=False)

def plot_returns(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['daily_return'], label='Daily Returns', color='green')
    plt.xlabel('Date')
    plt.ylabel('Daily Return')
    plt.title('Bitcoin Daily Returns Over Time')
    plt.legend()
    plt.grid(True)
    plt.show(block=False)

def plot_volatility(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['volatility'], label='Volatility', color='red')
    plt.xlabel('Date')
    plt.ylabel('Volatility (Annualized)')
    plt.title('Bitcoin Volatility Over Time')
    plt.legend()
    plt.grid(True)
    plt.show(block=False)

def plot_indicators(df):
    df['sma_50'] = calculate_sma(df, 50)
    df['sma_200'] = calculate_sma(df, 200)
    df['rsi'] = calculate_rsi(df)
    df['macd'], df['macd_signal'] = calculate_macd(df)
    
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['sma_50'], label='SMA 50', color='orange')
    plt.plot(df.index, df['sma_200'], label='SMA 200', color='purple')
    plt.plot(df.index, df['rsi'], label='RSI', color='cyan')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('Technical Indicators Over Time')
    plt.legend()
    plt.grid(True)
    plt.show(block=False)

def plot_signals(df):
    df['signal_score'] = calculate_trading_signal(df)
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['signal_score'], label='Trading Signal Score', color='purple')
    plt.xlabel('Date')
    plt.ylabel('Signal Score')
    plt.title('Trading Signal Score Over Time')
    plt.legend()
    plt.grid(True)
    plt.show(block=False)

if __name__ == "__main__":
    df = load_data()
    df = calculate_metrics(df)
    plot_price(df)
    plot_returns(df)
    plot_volatility(df)
    plot_indicators(df)  # Ensure indicators are calculated and plotted
    plot_signals(df)
    plt.show()  # Keeps all figures open

    # Calculate and display the latest trading signal
    latest_signal = get_latest_signal(df)
    print(f"Latest trading signal: {latest_signal}")