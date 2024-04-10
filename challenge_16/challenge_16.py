# Challenge 16

from PIL import Image, ImageChops
import numpy as np

image = Image.open("mozart.gif")
width, height = image.size
bar = [i for i, x in enumerate(image.histogram()) if x != 0 and not x % height][0]

for y in range(height):
    crop = 0, y, width, y + 1
    row = image.crop(crop)
    by = row.tobytes()
    i = by.index(bar)
    row = ImageChops.offset(row, -i)
    image.paste(row, crop)

image.save("challenge_16_output.png")

######################################
# OUTPUT:                            #
#                                    #
# IMAGE: see challenge_16_output.png #
######################################
