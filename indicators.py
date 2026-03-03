import pandas as pd

def sma(data, period=14):
    """
    Simple Moving Average
    """
    return data['close'].rolling(window=period).mean()


def rsi(data, period=14):
    """
    Relative Strength Index
    """
    delta = data['close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))
