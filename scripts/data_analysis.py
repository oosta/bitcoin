import pandas as pd
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import messagebox

def load_data():
    df = pd.read_csv('data/bitcoin_data.csv', index_col='timestamp', parse_dates=True)
    return df

def calculate_indicators(df):
    df['sma_50'] = df['price'].rolling(window=50).mean()
    df['sma_200'] = df['price'].rolling(window=200).mean()
    
    # RSI calculation
    delta = df['price'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['rsi'] = 100 - (100 / (1 + rs))

    # MACD calculation
    df['macd'] = df['price'].ewm(span=12, adjust=False).mean() - df['price'].ewm(span=26, adjust=False).mean()
    df['macd_signal'] = df['macd'].ewm(span=9, adjust=False).mean()

    return df

def calculate_trading_signals(df):
    df['buy_signal'] = ((df['rsi'] < 30) & (df['macd'] > df['macd_signal'])).astype(int)
    df['sell_signal'] = ((df['rsi'] > 70) & (df['macd'] < df['macd_signal'])).astype(int)
    df['signal_score'] = 50 + (df['buy_signal'] - df['sell_signal']) * 50
    return df

def plot_indicators(df):
    if not os.path.exists('plots'):
        os.makedirs('plots')

    plt.figure(figsize=(10, 5))
    plt.plot(df['price'], label='Bitcoin Price')
    plt.plot(df['sma_50'], label='SMA 50')
    plt.plot(df['sma_200'], label='SMA 200')
    plt.legend()
    plt.title('Bitcoin Price and Moving Averages')
    plt.savefig('plots/price_sma.png')

    plt.figure(figsize=(10, 5))
    plt.plot(df['rsi'], label='RSI')
    plt.legend()
    plt.title('RSI')
    plt.savefig('plots/rsi.png')

    plt.figure(figsize=(10, 5))
    plt.plot(df['macd'], label='MACD')
    plt.plot(df['macd_signal'], label='MACD Signal')
    plt.legend()
    plt.title('MACD')
    plt.savefig('plots/macd.png')

    plt.figure(figsize=(10, 5))
    plt.plot(df['signal_score'], label='Trading Signal Score')
    plt.legend()
    plt.title('Trading Signal Score')
    plt.savefig('plots/signal_score.png')

def make_decision(df):
    latest_data = df.iloc[-1]
    decision = "Hold"
    if latest_data['signal_score'] > 70:
        decision = "Strong Buy"
    elif latest_data['signal_score'] > 50:
        decision = "Buy"
    elif latest_data['signal_score'] < 30:
        decision = "Strong Sell"
    elif latest_data['signal_score'] < 50:
        decision = "Sell"

    summary = (
        f"Latest Bitcoin Price: {latest_data['price']}\n"
        f"SMA 50: {latest_data['sma_50']}\n"
        f"SMA 200: {latest_data['sma_200']}\n"
        f"RSI: {latest_data['rsi']}\n"
        f"MACD: {latest_data['macd']}\n"
        f"MACD Signal: {latest_data['macd_signal']}\n"
        f"Trading Signal Score: {latest_data['signal_score']}\n"
        f"Decision: {decision}"
    )

    # Display summary in a popup
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Bitcoin Trading Decision", summary)

def main():
    df = load_data()
    print("Loaded Data:")
    print(df.head())

    df = calculate_indicators(df)
    print("Technical Indicators:")
    print(df[['sma_50', 'sma_200', 'rsi', 'macd', 'macd_signal']].tail())

    df = calculate_trading_signals(df)
    print("Signal Calculation:")
    print(df[['buy_signal', 'sell_signal', 'signal_score']].tail())

    plot_indicators(df)
    make_decision(df)
    print("Analysis complete. Plots saved to 'plots' directory.")

if __name__ == "__main__":
    main()