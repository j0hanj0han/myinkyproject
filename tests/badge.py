#!/usr/bin/env python

import argparse

from PIL import Image, ImageFont, ImageDraw
from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium
from font_intuitive import Intuitive

print("""Inky pHAT/wHAT: Hello... my name is:

Use Inky pHAT/wHAT as a personalised name badge!

""")

# Command line arguments to set display type and colour, and enter your name

parser = argparse.ArgumentParser()
parser.add_argument('--mock', '-m', required=False, action='store_true', help="Simulate Inky using MatPlotLib")
parser.add_argument('--type', '-t', type=str, required=True, choices=["what", "phat"], help="type of display")
parser.add_argument('--colour', '-c', type=str, required=True, choices=["red", "black", "yellow"], help="ePaper display colour")
parser.add_argument('--name', '-n', type=str, required=True, help="Your name")
args = parser.parse_args()

if args.mock:
    from inky import InkyMockPHAT as InkyPHAT
    from inky import InkyMockWHAT as InkyWHAT
else:
    from inky import InkyWHAT, InkyPHAT

colour = args.colour

# Set up the correct display and scaling factors

if args.type == "phat":
    inky_display = InkyPHAT(colour)
    scale_size = 1
    padding = 0
elif args.type == "what":
    inky_display = InkyWHAT(colour)
    scale_size = 2.20
    padding = 15

# inky_display.set_rotation(180)
inky_display.set_border(inky_display.RED)

# Create a new canvas to draw on

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

# Load the fonts
intuitive_font = ImageFont.truetype(Intuitive, int(22 * scale_size))
hanken_bold_font = ImageFont.truetype(HankenGroteskBold, int(35 * scale_size))
hanken_medium_font = ImageFont.truetype(HankenGroteskMedium, int(16 * scale_size))

# Grab the name to be displayed

name = args.name

# Top and bottom y-coordinates for the white strip

y_top = int(inky_display.HEIGHT * (5.0 / 10.0))
y_bottom = y_top + int(inky_display.HEIGHT * (4.0 / 10.0))

# Draw the red, white, and red strips

for y in range(0, y_top):
    for x in range(0, inky_display.width):
        img.putpixel((x, y), inky_display.RED)

for y in range(y_top, y_bottom):
    for x in range(0, inky_display.width):
        img.putpixel((x, y), inky_display.WHITE)

for y in range(y_bottom, inky_display.HEIGHT):
    for x in range(0, inky_display.width):
        img.putpixel((x, y), inky_display.RED)

# Calculate the positioning and draw the "Hello" text

hello_w, hello_h = hanken_bold_font.getsize("Hello")
hello_x = int((inky_display.WIDTH - hello_w) / 2)
hello_y = 0 + padding
draw.text((hello_x, hello_y), "Hello", inky_display.WHITE, font=hanken_bold_font)

# Calculate the positioning and draw the "my name is" text
mynameis_w, mynameis_h = hanken_medium_font.getsize("my name is")
mynameis_x = int((inky_display.WIDTH - mynameis_w) / 2)
mynameis_y = hello_h + padding
draw.text((mynameis_x, mynameis_y), "my name is", inky_display.WHITE, font=hanken_medium_font)

# Calculate the positioning and draw the name text
name_w, name_h = intuitive_font.getsize(name)
name_x = int((inky_display.WIDTH - name_w) / 2)
name_y = int(y_top + ((y_bottom - y_top - name_h) / 2))
draw.text((name_x, name_y), name, inky_display.BLACK, font=intuitive_font)

# Display the completed name badge

inky_display.set_image(img)
inky_display.show()

if args.mock:
    print("Press Ctrl+C or close window to exit...")
    inky_display.wait_for_window_close()

