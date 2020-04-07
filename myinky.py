from PIL import Image, ImageFont, ImageDraw
from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium

# new drawing object
screen_width = 212
screen_height = 104
padding = 0
scale_size = 1
img = Image.new("P", (screen_width, screen_height))
draw = ImageDraw.Draw(img)

# message to show
def add_text(text_to_add=None):
    text = "Hello World !"
    font = ImageFont.load_default()
    # Calculate the positioning and draw the "Hello" text
    text_w, text_h = font.getsize(text)
    text_x = int((screen_width - text_w) / 2)
    text_y = 0 + padding
    print(text_x, text_y)
    draw.text(xy=(text_x, text_y),text=text, stroke_fill="black",fill="white", stroke_width=10, font=font ) 

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
        print(x)
        img.putpixel(xy=(x, 0), value=(0,0,0))
        img.putpixel(xy=(x, 103), value=(0,0,0))





# # Display the completed name badge
# inky_display.set_image(img)
# inky_display.show()


if __name__ == "__main__":
    add_text()
    draw_lines()
    #save the image 
    img.save("test1.png", "PNG")
