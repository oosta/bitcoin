# def calculate_signal(df):
#     df['buy_signal'] = 0
#     df['sell_signal'] = 0
#     df['signal_score'] = 50
    
#     for i in range(len(df)):
#         rsi = df['rsi'].iloc[i]
#         macd = df['macd'].iloc[i]
#         macd_signal = df['macd_signal'].iloc[i]
        
#         if rsi < 30 and macd > macd_signal:
#             df.at[df.index[i], 'buy_signal'] = 1
#         elif rsi > 70 and macd < macd_signal:
#             df.at[df.index[i], 'sell_signal'] = 1
            
#         df.at[df.index[i], 'signal_score'] = 50 + df['buy_signal'].sum() - df['sell_signal'].sum()
    
#     return df

# def get_latest_signal(df):
#     latest_row = df.iloc[-1]
#     score = latest_row['signal_score']
#     if score >= 75:
#         return f"{score} - Strong Buy"
#     elif score >= 55:
#         return f"{score} - Buy"
#     elif score <= 25:
#         return f"{score} - Strong Sell"
#     elif score <= 45:
#         return f"{score} - Sell"
#     else:
#         return f"{score} - Hold"
