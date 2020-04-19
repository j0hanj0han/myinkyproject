from PIL import Image, ImageFont, ImageDraw
from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium
import datetime
import requests
import time
import os

env = os.environ["ENV"]

if env == "PROD":
    from inky import InkyPHAT as InkyPHAT
    colour = "black"
    inky_display = InkyPHAT(colour)

class DisplayToInky:

    ''' Create an image with a text string object '''

    def __init__(self, text):
        if env == "PROD":
            self.screen_width = inky_display.WIDTH
            self.screen_height = inky_display.HEIGHT
        else:
            self.screen_width = 212
            self.screen_height = 104

        self.image = Image.new("P", (self.screen_width, self.screen_height))
        self.draw_object = ImageDraw.Draw(self.image)
        self.text = text
        self.write_text()
        self.borders = self.draw_borders()
        self.save_image()
        self.display_to_screen()
  
    def draw_borders(self):
        ''' Draw a simple border on the screen '''
        img = self.image
        y_top = int(self.screen_height)
        x_top = int(self.screen_width)
        for y in range(0, y_top):
            img.putpixel(xy=(0, y), value=(0, 0, 0))
            img.putpixel(xy=(211, y), value=(0, 0, 0))
        for x in range(0, x_top):
            img.putpixel(xy=(x, 0), value=(0, 0, 0))
            img.putpixel(xy=(x, 103), value=(0, 0, 0))
    
    def  write_text(self):
        text = self.text
        padding = 5
        font = ImageFont.load_default()
        text_w, text_h = font.getsize(text)
        text_x = int((self.screen_width - text_w) / 2)
        text_y = padding
        self.draw_object.text(
            xy=(text_x, text_y),
            text=text,
            stroke_fill="black",
            fill="white",
            stroke_width=10,
            font=font,
        )
    
    def save_image(self):
        img = self.image
        img.save("bonjour.png", "PNG")
    
    def display_to_screen(self):
        if env == "PROD":
            inky_display.set_image(self.image)
            inky_display.show()
        else:
            pass



if __name__ == "__main__":
    a = DisplayToInky("hello johan from the class")


# def add_meteo(city):
#     meteo = weatherstack.get_weather(city)
#     padding = 10
#     for element in meteo:
#         write_text(element, padding)
#         padding += 10


#         for city in cities:
#             img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
#             draw = ImageDraw.Draw(img)
#             add_meteo(city)
#             draw_lines()
#             # # Display the completed name badge





