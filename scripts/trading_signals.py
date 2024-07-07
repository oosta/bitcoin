import pandas as pd
from technical_indicators import calculate_sma, calculate_ema, calculate_rsi, calculate_macd

def calculate_trading_signal(df):
    df['sma_50'] = calculate_sma(df, 50)
    df['sma_200'] = calculate_sma(df, 200)
    df['rsi'] = calculate_rsi(df)
    df['macd'], df['macd_signal'] = calculate_macd(df)

    # Example criteria: simple conditions to combine indicators
    df['buy_signal'] = ((df['price'] > df['sma_50']) & (df['price'] > df['sma_200']) & (df['rsi'] < 30) & (df['macd'] > df['macd_signal'])).astype(int)
    df['sell_signal'] = ((df['price'] < df['sma_50']) & (df['price'] < df['sma_200']) & (df['rsi'] > 70) & (df['macd'] < df['macd_signal'])).astype(int)
    
    df['signal_score'] = 50 + (df['buy_signal'] * 50) - (df['sell_signal'] * 50)  # Score from 0 to 100
    return df['signal_score']

def get_latest_signal(df):
    signal_score = calculate_trading_signal(df)
    latest_signal = signal_score.iloc[-1]
    return latest_signal
