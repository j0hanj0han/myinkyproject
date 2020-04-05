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
hanken_bold_font = ImageFont.truetype(HankenGroteskBold, int(35 * scale_size))

# Calculate the positioning and draw the "Hello" text

hello_w, hello_h = hanken_bold_font.getsize("Hello")
hello_x = int((screen_width - hello_w) / 2)
hello_y = 0 + padding
draw.text((hello_x, hello_y),"white", "Hello") 

#save the image 
img.save("test.png", "PNG")


# # Display the completed name badge
# inky_display.set_image(img)
# inky_display.show()
