import MetaTrader5 as mt5
import pandas as pd

def get_data(symbol, timeframe, period):
    """Fetches historical data from MetaTrader 5."""
    data = mt5.copy_rates_from_pos(symbol, timeframe, 0, period)
    df = pd.DataFrame(data)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df.set_index('time', inplace=True)
    return df