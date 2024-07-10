import pandas as pd
import matplotlib.pyplot as plt
import os

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

    plt.figure(figsize=(10, 5))
    plt.plot(df['price'], label='Bitcoin Price')
    plt.plot(df['bollinger_mid'], label='Bollinger Mid')
    plt.plot(df['bollinger_upper'], label='Bollinger Upper')
    plt.plot(df['bollinger_lower'], label='Bollinger Lower')
    plt.legend()
    plt.title('Bollinger Bands')
    plt.savefig('plots/bollinger_bands.png')

    plt.figure(figsize=(10, 5))
    plt.plot(df['price'], label='Bitcoin Price', alpha=0.5)
    plt.scatter(df[df['buy_signal'] == 1].index, df[df['buy_signal'] == 1]['price'], label='Buy Signal', marker='^', color='g', alpha=1)
    plt.scatter(df[df['sell_signal'] == 1].index, df[df['sell_signal'] == 1]['price'], label='Sell Signal', marker='v', color='r', alpha=1)
    plt.legend()
    plt.title('Bitcoin Price with Buy/Sell Signals')
    plt.savefig('plots/price_with_signals.png')

def plot_google_trends(df):
    if not os.path.exists('plots'):
        os.makedirs('plots')

    fig, ax1 = plt.subplots(figsize=(10, 5))

    ax1.set_xlabel('Date')
    ax1.set_ylabel('Bitcoin Price', color='tab:blue')
    ax1.plot(df.index, df['price'], label='Bitcoin Price', color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    ax2 = ax1.twinx()
    ax2.set_ylabel('Google Trends', color='tab:orange')
    ax2.plot(df.index, df['google_trends'], label='Google Trends', color='tab:orange')
    ax2.tick_params(axis='y', labelcolor='tab:orange')

    fig.tight_layout()
    plt.title('Bitcoin Price and Google Trends Overlay')
    plt.legend(loc='upper left')
    plt.savefig('plots/price_google_trends.png')
