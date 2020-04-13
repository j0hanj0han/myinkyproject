import binance_calls as bc 

def display_price(pair):
    '''return pair and symbol'''
    price = bc.get_last_price(pair)
    result = f"{pair}: {price} USDT"
    return result

if __name__ == "__main__":
    pairs=['BTCUSDT', 'ETHUSDT', 'LTCUSDT', 'LINKUSDT']
    result = []
    for pair in pairs:
        price = display_price(pair)
        result.append(price)
    print(result)
