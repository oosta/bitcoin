# import pandas as pd

# def calculate_sma(df, window):
#     return df['price'].rolling(window=window).mean()

# def calculate_rsi(df, window=14):
#     delta = df['price'].diff()
#     gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
#     loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
#     rs = gain / loss
#     df['rsi'] = 100 - (100 / (1 + rs))
#     return df

# def calculate_macd(df, short_window=12, long_window=26, signal_window=9):
#     df['ema_short'] = df['price'].ewm(span=short_window, adjust=False).mean()
#     df['ema_long'] = df['price'].ewm(span=long_window, adjust=False).mean()
#     df['macd'] = df['ema_short'] - df['ema_long']
#     df['macd_signal'] = df['macd'].ewm(span=signal_window, adjust=False).mean()
#     return df

# def calculate_indicators(df):
#     df['sma_50'] = calculate_sma(df, 50)
#     df['sma_200'] = calculate_sma(df, 200)
#     df = calculate_rsi(df, 14)
#     df = calculate_macd(df)
#     return df
