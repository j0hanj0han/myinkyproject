from myinkyproject.binance import binance
from myinkyproject.inky import inky

if __name__ == "__main__":
    binance.get_last_price('BTCUSDT')
    inky.write_text()
    pass