def run_backtest(data, initial_balance):
    """
    Simple backtesting engine.
    """
    balance = initial_balance
    position = 0

    for i in range(len(data)):
        signal = data['signal'][i]
        price = data['close'][i]

        if signal == "BUY" and balance > 0:
            position = balance / price
            balance = 0

        elif signal == "SELL" and position > 0:
            balance = position * price
            position = 0

    final_balance = balance + (position * data['close'].iloc[-1])
    return final_balance
