from indicators import sma, rsi

def apply_strategy(data):
    """
    SMA crossover + RSI confirmation strategy.
    """

    data['sma_fast'] = sma(data, 10)
    data['sma_slow'] = sma(data, 30)
    data['rsi'] = rsi(data, 14)

    signals = []

    for i in range(len(data)):
        if data['sma_fast'][i] > data['sma_slow'][i] and data['rsi'][i] < 70:
            signals.append("BUY")
        elif data['sma_fast'][i] < data['sma_slow'][i] and data['rsi'][i] > 30:
            signals.append("SELL")
        else:
            signals.append("HOLD")

    data['signal'] = signals
    return data
