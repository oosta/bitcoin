import pandas as pd

def calculate_sma(df, window):
    return df['price'].rolling(window=window).mean()

def calculate_ema(df, window):
    return df['price'].ewm(span=window, adjust=False).mean()

def calculate_rsi(df, window=14):
    delta = df['price'].diff()
    gain = (delta.where(delta > 0, 0)).fillna(0)
    loss = (-delta.where(delta < 0, 0)).fillna(0)
    
    avg_gain = gain.rolling(window=window, min_periods=1).mean()
    avg_loss = loss.rolling(window=window, min_periods=1).mean()
    
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_macd(df, short_window=12, long_window=26, signal_window=9):
    short_ema = calculate_ema(df, short_window)
    long_ema = calculate_ema(df, long_window)
    macd = short_ema - long_ema
    signal = macd.ewm(span=signal_window, adjust=False).mean()
    return macd, signal
