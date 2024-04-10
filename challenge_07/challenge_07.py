# Challenge 7

from PIL import Image
import re


def get_colors(image_path):
    image = Image.open(image_path)
    colors = [image.getpixel((1 + i, 50))[0] for i in range(1, image.width, 7)]
    return colors[:-3]


image_path = "oxygen.png"
colors = get_colors(image_path)

message = "".join(chr(x) for x in colors)
print(message)

result = re.findall(r"\d+", message)
print("".join(chr(x) for x in map(int, result)))

###########################################################################################
# OUTPUT:                                                                                 #
#                                                                                         #
# smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121] #
# integrity                                                                               #
###########################################################################################
