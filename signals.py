def generate_signals(df):
    """Generates buy and sell signals."""
    df['Position'] = 0
    df.loc[(df['close'] > df['SMA_50']) & 
           (df['close'] > df['SMA_100']) & 
           (df['close'] > df['SMA_200']) & 
           (df['RSI'] > 50) & 
           (df['Fractals_Down'] != 0), 'Position'] = 1  # Buy signal
    df.loc[(df['close'] < df['SMA_50']) & 
           (df['close'] < df['SMA_100']) & 
           (df['close'] < df['SMA_200']) & 
           (df['RSI'] < 50) & 
           (df['Fractals_Up'] != 0), 'Position'] = -1 # Sell signal
    return df