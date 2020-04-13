import binance_calls as bc 

def display_price(pairs_list):
    '''return pair and symbol'''
    result = []
    for pair in pairs_list:
        price = round(float(bc.get_last_price(pair)),2)
        price = f"{pair}: {price} USDT"
        result.append(price)
    return result

# if __name__ == "__main__":
#     pairs=['BTCUSDT', 'ETHUSDT', 'LTCUSDT', 'LINKUSDT']
#     result = []
#     for pair in pairs:
#         price = display_price(pair)
#         result.append(price)
#     print(result)
