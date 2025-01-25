import MetaTrader5 as mt5

def place_order(symbol, order_type, volume, stop_loss):
    """Places an order with MetaTrader 5."""
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume,
        "type": order_type,
        "price": mt5.symbol_info_tick(symbol).ask if order_type == mt5.ORDER_TYPE_BUY else mt5.symbol_info_tick(symbol).bid,
        "deviation": 10,
        "magic": 234000,
        "comment": "Scalper Bot",
        "type_time": mt5.TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_RETURN,
        "stoploss": stop_loss,
    }
    result = mt5.order_send(request)
    if result != None:
        print(f"Order send result for {symbol}:", result)
    else:
        print(f"Order send failed for {symbol}, error code =", mt5.last_error())
    return result

def close_position(position_id):
    """Closes an existing position."""
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "ticket": position_id,
        "type": mt5.ORDER_TYPE_SELL if position_id > 0 else mt5.ORDER_TYPE_BUY, 
        "volume": mt5.positions_get(ticket=position_id)[0].volume,
        "deviation": 10,
        "magic": 234000,
        "comment": "Scalper Bot - Close",
        "type_time": mt5.TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_RETURN,
    }
    result = mt5.order_send(request)
    if result != None:
        print(f"Position closed: {position_id}")
    else:
        print(f"Position closing failed, error code =", mt5.last_error())