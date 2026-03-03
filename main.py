import pandas as pd
from strategy import apply_strategy
from backtester import run_backtest
from config import INITIAL_BALANCE

def load_data():
    """
    Load historical data from CSV.
    CSV must contain: timestamp, open, high, low, close, volume
    """
    return pd.read_csv("data.csv")


def main():
    data = load_data()
    data = apply_strategy(data)

    final_balance = run_backtest(data, INITIAL_BALANCE)

    print("Initial Balance:", INITIAL_BALANCE)
    print("Final Balance:", round(final_balance, 2))


if __name__ == "__main__":
    main()
