from PIL import Image, ImageFont, ImageDraw

# new drawing object
screen_width = ""
screen_height =""
img = Image.new("P", (screen_width, screen_height))
draw = ImageDraw.Draw(img)

# message to show
text = "Hello"
text_w, text_h = hanken_bold_font.getsize(text)

hello_x = int((inky_display.WIDTH - hello_w) / 2)
hello_y = 0 + padding

#draw
draw.text((text_x, text_y), text, inky_display.WHITE, font=hanken_bold_font)


#save the image 
img.save("test.png", "PNG")


# # Display the completed name badge
# inky_display.set_image(img)
# inky_display.show()