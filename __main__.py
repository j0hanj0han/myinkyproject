from myinkyproject.mybinance import binance
from myinkyproject.myinky import inky

if __name__ == "__main__":
    BTC = binance.get_last_price('BTCUSDT')
    inky.DisplayToInky(str(BTC))
    #inky.write_text()
    pass