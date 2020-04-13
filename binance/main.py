from PIL import Image, ImageFont, ImageDraw
from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium
import datetime
import requests
import time
import prices

# from inky import InkyPHAT as InkyPHAT
# colour = "black"
# inky_display = InkyPHAT(colour)

# new drawing object
screen_width = 212
screen_height = 104
# screen_width = inky_display.WIDTH
# screen_height = inky_display.HEIGHT
img = Image.new("P", (screen_width, screen_height))

def write_text(text, padding):
    text = text
    font = ImageFont.load_default()
    text_w, text_h = font.getsize(text)
    text_x = int((screen_width - text_w) / 2)
    text_y = padding
    draw.text(
        xy=(text_x, text_y),
        text=text,
        stroke_fill="black",
        fill="white",
        stroke_width=10,
        font=font,
    )
def draw_lines():
    # draw a border around the screen
    # Top and bottom y-coordinates for the white strip
    y_top = int(screen_height)
    x_top = int(screen_width)

    for y in range(0, y_top):
        img.putpixel(xy=(0, y), value=(0, 0, 0))
        # split in two frame
        # img.putpixel(xy=(103, y), value=(0,0,0))
        img.putpixel(xy=(211, y), value=(0, 0, 0))
    for x in range(0, x_top):
        img.putpixel(xy=(x, 0), value=(0, 0, 0))
        img.putpixel(xy=(x, 103), value=(0, 0, 0))


def add_prices(pairs_list):
    prices_list = prices.display_price(pairs_list)
    padding = 5 
    for price in prices_list:
        write_text(price, padding)
        padding +=10
    

if __name__ == "__main__":
    img = Image.new("P", (screen_width, screen_height))
    draw = ImageDraw.Draw(img)
    my_list=['BTCUSDT', 'ETHUSDT', 'LTCUSDT', 'LINKUSDT']
    add_prices(my_list)
    draw_lines()
    img.save("binance_prices.png", "PNG")




