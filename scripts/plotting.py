import matplotlib.pyplot as plt

def plot_indicators(df):
    # Plot Bitcoin price with buy/sell signals
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['price'], label='Bitcoin Price', alpha=0.5)

    plt.scatter(df[df['buy_signal'] == 1].index, df[df['buy_signal'] == 1]['price'], label='Buy Signal', color='lightgreen', marker='^', alpha=1)
    plt.scatter(df[df['sell_signal'] == 1].index, df[df['sell_signal'] == 1]['price'], label='Sell Signal', color='orange', marker='v', alpha=1)
    plt.scatter(df[df['strong_buy_signal'] == 1].index, df[df['strong_buy_signal'] == 1]['price'], label='Strong Buy Signal', color='green', marker='^', alpha=1)
    plt.scatter(df[df['strong_sell_signal'] == 1].index, df[df['strong_sell_signal'] == 1]['price'], label='Strong Sell Signal', color='red', marker='v', alpha=1)

    plt.title('Bitcoin Price with Trading Signals')
    plt.xlabel('Date')
    plt.ylabel('Price (CAD)')
    plt.legend()
    plt.grid()
    plt.savefig('plots/price_with_signals.png')
    plt.close()

    # Plot MACD
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['macd'], label='MACD', color='blue', alpha=0.5)
    plt.plot(df.index, df['macd_signal'], label='MACD Signal', color='red', alpha=0.5)

    plt.title('MACD and MACD Signal')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid()
    plt.savefig('plots/macd.png')
    plt.close()

    # Plot RSI
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['rsi'], label='RSI', color='purple', alpha=0.5)

    plt.title('RSI')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid()
    plt.savefig('plots/rsi.png')
    plt.close()

    # Plot Bollinger Bands
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['price'], label='Bitcoin Price', alpha=0.5)
    plt.plot(df.index, df['bollinger_mid'], label='Bollinger Mid', color='blue', alpha=0.5)
    plt.plot(df.index, df['bollinger_upper'], label='Bollinger Upper', color='green', alpha=0.5)
    plt.plot(df.index, df['bollinger_lower'], label='Bollinger Lower', color='red', alpha=0.5)

    plt.title('Bollinger Bands')
    plt.xlabel('Date')
    plt.ylabel('Price (CAD)')
    plt.legend()
    plt.grid()
    plt.savefig('plots/bollinger_bands.png')
    plt.close()

def plot_google_trends(df):
    # Plot Google Trends data overlaying Bitcoin Price
    fig, ax1 = plt.subplots(figsize=(12, 6))

    ax1.set_xlabel('Date')
    ax1.set_ylabel('Bitcoin Price (CAD)', color='tab:green')
    ax1.plot(df.index, df['price'], label='Bitcoin Price', color='tab:green', alpha=0.5)
    ax1.tick_params(axis='y', labelcolor='tab:green')

    ax2 = ax1.twinx()
    ax2.set_ylabel('Google Trends', color='tab:blue')
    ax2.plot(df.index, df['google_trends'], label='Google Trends', color='tab:blue', alpha=0.5)
    ax2.tick_params(axis='y', labelcolor='tab:blue')

    fig.tight_layout()
    plt.title('Bitcoin Price vs Google Trends')
    plt.legend()
    plt.grid()
    plt.savefig('plots/price_vs_google_trends.png')
    plt.close()

    # Plot for the strong buy signals only:
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['price'], label='Bitcoin Price', alpha=0.5)
    plt.scatter(df[df['strong_buy_signal'] == 1].index, df[df['strong_buy_signal'] == 1]['price'], label='Strong Buy Signal', color='green', marker='^', alpha=1)

    plt.title('Strong Buy Signals')
    plt.xlabel('Date')
    plt.ylabel('Price (CAD)')
    plt.legend()
    plt.grid()
    plt.savefig('plots/strong_buy_signals.png')
    plt.close()

