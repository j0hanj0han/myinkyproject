from PIL import Image, ImageFont, ImageDraw
import myinkylib
import datetime
import requests
import time
import prices

def add_prices(pairs_list):
    img = Image.new("P", (212, 104))
    draw = ImageDraw.Draw(img)

    prices_list = prices.display_price(pairs_list)
    padding = 5 
    for price in prices_list:
        myinkylib.write_text(price, padding, draw)
        padding +=10
    
    myinkylib.draw_lines(img)
    img.save("binance_prices.png", "PNG")

if __name__ == "__main__":
    my_list=['BTCUSDT', 'ETHUSDT', 'LTCUSDT', 'LINKUSDT']
    add_prices(my_list)

if __name__ == "__main__":
    my_list=['BTCUSDT', 'ETHUSDT', 'LTCUSDT', 'LINKUSDT']
    while True:
        add_prices(my_list)
        time.sleep(10)



