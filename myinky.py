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
text = "Hello World !"
font = ImageFont.load_default()


# Calculate the positioning and draw the "Hello" text

text_w, text_h = font.getsize(text)
text_x = int((screen_width - text_w) / 2)
text_y = 0 + padding
print(text_x, text_y)
draw.text(xy=(text_x, text_y),text=text, stroke_fill="black",fill="white", stroke_width=10, font=font ) 

#save the image 
img.save("test.png", "PNG")


# # Display the completed name badge
# inky_display.set_image(img)
# inky_display.show()
