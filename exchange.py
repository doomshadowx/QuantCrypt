import ccxt

def connect_exchange(api_key, api_secret):
    """
    Connect to exchange using CCXT.
    """
    exchange = ccxt.binance({
        'apiKey': api_key,
        'secret': api_secret
    })
    return exchange
