import pandas as pd
import tkinter as tk
from tkinter import messagebox
from plotting import plot_indicators, plot_google_trends

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

    # Bollinger Bands
    df['bollinger_mid'] = df['price'].rolling(window=20).mean()
    df['bollinger_std'] = df['price'].rolling(window=20).std()
    df['bollinger_upper'] = df['bollinger_mid'] + (df['bollinger_std'] * 2)
    df['bollinger_lower'] = df['bollinger_mid'] - (df['bollinger_std'] * 2)

    # On-Balance Volume (OBV)
    df['obv'] = (df['volume'] * (delta.apply(lambda x: 1 if x > 0 else -1))).cumsum()

    return df

def calculate_trading_signals(df):
    # Define weights for each indicator
    weight_rsi = 0.2
    weight_macd = 0.2
    weight_bollinger = 0.2
    weight_fear_greed = 0.2
    weight_volume = 0.1
    weight_trends = 0.1

    # Calculate individual scores
    rsi_score = ((df['rsi'] < 30) * weight_rsi) - ((df['rsi'] > 70) * weight_rsi)
    macd_score = ((df['macd'] > df['macd_signal']) * weight_macd) - ((df['macd'] < df['macd_signal']) * weight_macd)
    bollinger_score = ((df['price'] < df['bollinger_lower']) * weight_bollinger) - ((df['price'] > df['bollinger_upper']) * weight_bollinger)
    fear_greed_score = ((df['fear_greed'] < 30) * weight_fear_greed) - ((df['fear_greed'] > 70) * weight_fear_greed)
    volume_score = ((df['volume'] > df['volume'].rolling(window=20).mean()) * weight_volume) - ((df['volume'] < df['volume'].rolling(window=20).mean()) * weight_volume)
    trends_score = ((df['google_trends'] > df['google_trends'].rolling(window=20).mean()) * weight_trends) - ((df['google_trends'] < df['google_trends'].rolling(window=20).mean()) * weight_trends)

    # Combine scores to calculate the overall trading signal score
    df['signal_score'] = 50 + 50 * (rsi_score + macd_score + bollinger_score + fear_greed_score + volume_score + trends_score)

    # Define buy and sell signals based on the combined score
    df['buy_signal'] = (df['signal_score'] > 60).astype(int)
    df['sell_signal'] = (df['signal_score'] < 40).astype(int)

    return df

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
        f"Bollinger Upper: {latest_data['bollinger_upper']}\n"
        f"Bollinger Lower: {latest_data['bollinger_lower']}\n"
        f"Fear and Greed Index: {latest_data['fear_greed']}\n"
        f"Volume: {latest_data['volume']}\n"
        f"Google Trends: {latest_data['google_trends']}\n"
        f"Trading Signal Score: {latest_data['signal_score']}\n"
        f"Decision: {decision}"
    )

    # Display summary in a popup
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Bitcoin Trading Decision", summary)

def backtest_strategy(df):
    initial_balance = 10000  # Initial balance in CAD
    balance = initial_balance
    bitcoin_held = 0
    for i in range(len(df)):
        if df['buy_signal'].iloc[i] == 1 and balance > 0:
            # Buy Bitcoin
            bitcoin_held = balance / df['price'].iloc[i]
            balance = 0
        elif df['sell_signal'].iloc[i] == 1 and bitcoin_held > 0:
            # Sell Bitcoin
            balance = bitcoin_held * df['price'].iloc[i]
            bitcoin_held = 0

    final_balance = balance + (bitcoin_held * df['price'].iloc[-1])
    profit_loss = final_balance - initial_balance

    print(f"Initial Balance: ${initial_balance:.2f} CAD")
    print(f"Final Balance: ${final_balance:.2f} CAD")
    print(f"Profit/Loss: ${profit_loss:.2f} CAD")

def main():
    df = load_data()
    print("Loaded Data:")
    print(df.head())

    df = calculate_indicators(df)
    print("Technical Indicators:")
    print(df[['sma_50', 'sma_200', 'rsi', 'macd', 'macd_signal', 'bollinger_mid', 'bollinger_upper', 'bollinger_lower', 'fear_greed', 'volume', 'obv']].tail())

    df = calculate_trading_signals(df)
    print("Signal Calculation:")
    print(df[['buy_signal', 'sell_signal', 'signal_score']].tail())

    # Plot indicators and Google Trends
    plot_indicators(df)
    plot_google_trends(df)

    make_decision(df)
    backtest_strategy(df)
    print("Analysis complete. Plots saved to 'plots' directory.")

if __name__ == "__main__":
    main()