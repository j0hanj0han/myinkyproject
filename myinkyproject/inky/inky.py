from PIL import Image, ImageFont, ImageDraw
from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium
import datetime
import weatherstack
import requests
import time

from inky import InkyPHAT as InkyPHAT
colour = "black"
inky_display = InkyPHAT(colour)

# new drawing object
# screen_width = 212
# screen_height = 104
screen_width = inky_display.WIDTH
screen_height = inky_display.HEIGHT
#img = Image.new("P", (screen_width, screen_height))




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


# message to show
def add_text(text_to_add=None):
    text = "Hello Johan !"
    write_text(text, 5)


def add_time():
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")
    write_text(now, 20)


def add_meteo(city):
    meteo = weatherstack.get_weather(city)
    padding = 10
    for element in meteo:
        write_text(element, padding)
        padding += 10


if __name__ == "__main__":

    # add_text()
    # add_meteo()
    # draw_lines()
    # img.save("test.png", "PNG")
    cities = ["Montpellier", "Paris", "Argences", "La Batie-Neuve"]
    while True: 
        for city in cities:
            img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
            draw = ImageDraw.Draw(img)
            add_meteo(city)
            draw_lines()
            # # Display the completed name badge
            inky_display.set_image(img)
            inky_display.show()
            time.sleep(30)



