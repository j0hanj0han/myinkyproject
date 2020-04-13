#!/usr/bin/python3
import re
import os
import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path
from binance.client import Client

# Secret for Binance
API_KEY = os.environ["API_KEY"]
SECRET_KEY = os.environ["SECRET_KEY"]
client = Client(API_KEY, SECRET_KEY)
cwd = os.getcwd()

def get_keys():
    
    keys = [
    "datetime",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "close_time",
    "quote_asset_volume",
    "number_of_trade",
    "taker_buy_base_asset_volume",
    "taker_buy_quote_asset_volume",
    "ignore",
    ]
    return keys

def get_market_pairs(pair):
    prices = client.get_all_tickers()
    # list all pairs in list
    PAIRS = []
    [PAIRS.append(prices[i]["symbol"]) for i in range(len(prices))]
    # PAIR matching
    r = re.compile(f".*{pair}")
    pairs_possible = list(filter(r.match, PAIRS))
    print("nb of pairs possible ", len(pairs_possible))
    print("pairs possible ", pairs_possible)
    return PAIRS


def get_market_data(symbol, interval, start_str):
    # get the kline data
    raw_data = client.get_historical_klines(
        symbol=symbol, interval=interval, start_str=start_str
    )
    # create a list of dictionnary with the keys belows:  
    
    data_with_headers = []
    for kline in raw_data:
        values = kline
        new_dict = dict(zip(get_keys(), values))
        data_with_headers.append(new_dict)

    # changing the date in the dict
    for kline in data_with_headers:
        # kline["datetime"] = datetime.fromtimestamp(int(kline["datetime"]) / 1000)
        # kline["close_time"] = datetime.fromtimestamp(int(kline["close_time"]) / 1000)
        # kline["datetime"] = (int(kline["datetime"]) / 1000)
        # kline["close_time"] = (int(kline["close_time"]) / 1000)
        #timedelta for UTC
        kline["datetime"] = (datetime.fromtimestamp(int(kline["datetime"]) / 1000))
        kline["close_time"] =( datetime.fromtimestamp(int(kline["close_time"]) / 1000))

    # create a dataframe
    if len(data_with_headers ) > 0: 
        dataframe = pd.DataFrame.from_dict(data_with_headers[0], orient="index")
        for data in data_with_headers:
            dataframe[data_with_headers.index(data)] = data_with_headers[
                data_with_headers.index(data)
            ].values()

        dataframe = dataframe.transpose()
        dataframe = dataframe.set_index("datetime")
        dataframe = dataframe.sort_values(["datetime"], ascending=[1])

        #dataframe['time'] = [d.time() for d in dataframe.index]
        #dataframe.index = [d.date() for d in dataframe.index]
        #dataframe.rename(index={0:'datetime'})
        
        #cols= dataframe.columns.tolist()
        #cols = cols[-1:] + cols[:-1]
        #dataframe = dataframe[cols]

        #import pdb; pdb.set_trace()
        # parent_dir = Path(cwd).parent
        # dataframe.to_csv(f"{parent_dir}/data/{symbol}_data.csv")

        # skip the last row because interval is not finish
        print(dataframe)
        print("--------------------------------------")
        dataframe.drop(dataframe.tail(1).index, inplace=True)
        print(dataframe)
        df_list = dataframe.reset_index().values.tolist()
        #import pdb; pdb.set_trace()
        #print(dataframe.head(5))
        #print(dataframe.tail(5))
        return df_list
    else:
        print("No DATA to insert")
        df_list = []
        return df_list
    

    #return dataframe


def get_btc_price():
    prices = client.get_all_tickers()
    for asset in prices:
        if asset["symbol"] == "BTCUSDT":
            btc_price = asset["price"]
            print(btc_price)
    return btc_price

def get_last_price(symbol):
    prices = client.get_all_tickers()
    for asset in prices:
        if asset["symbol"] == symbol:
            symbol_price = asset["price"]
            print(symbol, symbol_price)
    return symbol_price


def get_my_portfolio():
    # get quantity of pairs owned and delete if quantity is null
    portfolio_quantity = []
    balances = client.get_account()["balances"]
    prices = client.get_all_tickers()

    for asset in balances:
        if float(asset["free"]) + float(asset["locked"]) != 0:
            asset_owned = [
                asset["asset"],
                float(asset["free"]) + float(asset["locked"]),
            ]
            portfolio_quantity.append(asset_owned)
    # print("portfolio quantity, ", portfolio_quantity)

    # replace symbol by pair USDT
    for asset in portfolio_quantity:
        if asset[0] != "USDT":
            asset[0] = f"{asset[0]}USDT"
            
    # check each price for the trading pair possible list.
    for price in prices:
        for asset in portfolio_quantity:
            if asset[0] == price["symbol"]:
                price_found = price["price"]
                asset.append(price_found)
    # print("portfolio quantity with price", portfolio_quantity)

    # insert data in a Dataframe and calculate the total
    df = pd.DataFrame(
        portfolio_quantity,
        index=[symbol[0] for symbol in portfolio_quantity],
        columns=["SYMBOL", "QUANTITY", "PRICE"],
    )
    df["QUANTITY"] = df["QUANTITY"].astype(float)
    df["PRICE"] = df["PRICE"].astype(float)
    df["PRICE"] = df["PRICE"].fillna(1)
    df["TOTAL"] = df["QUANTITY"] * df["PRICE"]

    dollars_owned = str(df["TOTAL"].sum())
    # display the total of the portfolio
    print(df)
    print("johan your dols are : ", df["TOTAL"].sum())
    return df.to_csv()

def get_volume_data(symbol, frequency, sma):
    # get the df with volume

    # get the kline data
    raw_data = client.get_historical_klines(
        symbol=symbol, interval="4h", start_str="1 months ago UTC"
    )
    for kline in raw_data:
        kline[0] = datetime.fromtimestamp(int(kline[0]) / 1000)

    # create a list of dictionnary with the keys belows:

    df = pd.DataFrame(columns=keys, data=raw_data)

    df["datetime"] = pd.to_datetime(df["datetime"])
    # df = df.set_index('datetime')
    df = df[["datetime", "volume"]]
    df = df.set_index("datetime")
    df = df.astype("float")
    df = df.resample(frequency).sum()
    df["variation"] = df.pct_change(fill_method="ffill")
    df["SMA"] = df.variation.rolling(sma).mean()
    df["% diff more than 20% of SMA"] = (df["variation"] / df["SMA"]) > 1.2
    print(df)

def get_orderbook_ticker(symbol):
    tickers = client.get_orderbook_tickers()
    for ticker in tickers:
        # print(ticker)
        if ticker["symbol"] == symbol:
            result = ticker
            print(result)

def get_best_variation_24h():
    # 24h change
    tickers = client.get_ticker()
    columns = list(tickers[0])
    df = pd.DataFrame(columns=columns, data=tickers)
    df = df.sort_values(by="priceChangePercent", ascending=False)
    df.to_csv("24h")
    print(df)

def get_best_price_variation(symbol, interval, start_str, resample):

    # get the kline data
    raw_data = client.get_historical_klines(
        symbol=symbol, interval=interval, start_str=start_str
    )
    for kline in raw_data:
        kline[0] = datetime.fromtimestamp(int(kline[0]) / 1000)

    # create a list of dictionnary with the keys belows:
    df = pd.DataFrame(columns=keys, data=raw_data)
    df["datetime"] = pd.to_datetime(df["datetime"])
    df = df[["datetime", "open"]]
    df = df.set_index("datetime")
    df = df.astype("float")
    df = df.resample(resample).mean()

    # df['variation'] = df.pct_change(1)
    df["SMA 5"] = df.open.rolling(5).mean()
    df["SMA 10"] = df.open.rolling(10).mean()
    print(df)

def get_close_prices(symbol, interval, start_str):
    closes = []
    for kline in client.get_historical_klines_generator(
        symbol=symbol, interval=interval, start_str=start_str
    ):
        kline_dict = dict(zip(get_keys(), kline))
        # print('closes :', kline_dict['close'])
        closes.append(float(kline_dict["close"]))
    # print(f"------{symbol}-------")
    # print(np.asarray(closes))
    return np.asarray(closes)


#get_market_pairs('USDT')
#get_btc_price()
#get_market_data('BTCUSDT', '1m', '2020-03-17 22:38:00 UTC+1')
# get_close_prices('BTCUSDT', '1h', '3 weeks ago')

