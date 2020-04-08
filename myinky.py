from PIL import Image, ImageFont, ImageDraw
from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium
import datetime
# from inky import InkyMockPHAT as InkyPHAT
# colour = "black"
# inky_display = InkyPHAT(colour)

# new drawing object
screen_width = 212
screen_height = 104
padding = 0
scale_size = 1
img = Image.new("P", (screen_width, screen_height))
#img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))


draw = ImageDraw.Draw(img)

# message to show
def add_text(text_to_add=None):
    text = "Hello Johan !"
    font = ImageFont.load_default()
    # Calculate the positioning and draw the "Hello" text
    text_w, text_h = font.getsize(text)
    text_x = int((screen_width - text_w) / 2)
    text_y = 5 + padding
    draw.text(xy=(text_x, text_y),text=text, stroke_fill="black",fill="white", stroke_width=10, font=font ) 

def add_time():
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")
    font = ImageFont.load_default()
    now_w, now_h = font.getsize(now)
    now_x = int((screen_width - now_w) / 2)
    now_y = 20 + padding
    draw.text(xy=(now_x, now_y), text=now, stroke_fill="black", fill="white",stroke_width=10,font=font)


def draw_lines():
    # draw a border around the screen
    # Top and bottom y-coordinates for the white strip
    y_top = int(screen_height)
    x_top = int(screen_width)

    print(x_top, y_top)
    # Draw the red, white, and red strips
    for y in range(0, y_top):
        img.putpixel(xy=(0, y), value=(0,0,0))
        #split in two frame
        #img.putpixel(xy=(103, y), value=(0,0,0))
        img.putpixel(xy=(211, y), value=(0,0,0))


    for x in range(0, x_top):
        img.putpixel(xy=(x, 0), value=(0,0,0))
        img.putpixel(xy=(x, 103), value=(0,0,0))





# # Display the completed name badge
# inky_display.set_image(img)
# inky_display.show()


if __name__ == "__main__":
    add_text()
    add_time()
    draw_lines()
    #save the image 
    img.save("test1.png", "PNG")
