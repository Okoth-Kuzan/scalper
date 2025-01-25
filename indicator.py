import talib

def calculate_indicators(df):
    """Calculates technical indicators."""
    df['SMA_50'] = df['close'].rolling(window=50).mean()
    df['SMA_100'] = df['close'].rolling(window=100).mean()
    df['SMA_200'] = df['close'].rolling(window=200).mean()
    df['RSI'] = talib.RSI(df['close'], timeperiod=14)
    df['Fractals_Up'] = talib.FRAC(df['high'], timeperiod=3)
    df['Fractals_Down'] = talib.FRAC(-df['low'], timeperiod=3)
    return df