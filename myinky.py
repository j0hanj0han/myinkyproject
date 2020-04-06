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
    # Top and bottom y-coordinates for the white strip
    y_top = int(screen_height)
    y_bottom = y_top + int(screen_height * (4.0 / 10.0))
    print("ytop", y_top)
    print("ybottom", y_bottom)
    # Draw the red, white, and red strips
    for y in range(0, y_top):
        for x in range(0, int(screen_width/2)):
            print(type((x,y)))
            img.putpixel(xy=(x, y), value=(0,0,0))


# # Display the completed name badge
# inky_display.set_image(img)
# inky_display.show()


if __name__ == "__main__":
    add_text()
    draw_lines()
    #save the image 
    img.save("test.png", "PNG")
