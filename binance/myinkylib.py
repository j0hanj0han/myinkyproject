from PIL import Image, ImageFont, ImageDraw
from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium
# from inky import InkyPHAT as InkyPHAT
# colour = "black"
# inky_display = InkyPHAT(colour)

# new drawing object
screen_width = 212
screen_height = 104
# screen_width = inky_display.WIDTH
# screen_height = inky_display.HEIGHT
# img = Image.new("P", (screen_width, screen_height))
# draw = ImageDraw.Draw(img)

def write_text(text, padding, draw_object):
    text = text
    font = ImageFont.load_default()
    text_w, text_h = font.getsize(text)
    #text_x = int((screen_width - text_w) / 2)
    text_x = 5
    text_y = padding
    draw_object.text(
        xy=(text_x, text_y),
        text=text,
        stroke_fill="black",
        fill="white",
        stroke_width=10,
        font=font,
    )
def draw_lines(img):
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
