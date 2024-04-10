# Challenge 9

from PIL import Image, ImageDraw
from itertools import pairwise

with open("first.txt") as f:
    first = [*map(int, f.read().replace("\n", "").split(","))]

with open("second.txt") as f:
    second = [*map(int, f.read().replace("\n", "").split(","))]

coordinates = [[*zip(*[iter(first)] * 2)], [*zip(*[iter(second)] * 2)]]
size = max(first + second) + min(first + second)

image = Image.new("RGB", [size] * 2, "white")
draw = ImageDraw.Draw(image)

for coordinate in coordinates:
    for a, b in pairwise(coordinate):
        draw.line([a, b], fill="black", width=2)

image.save("challenge_09_output.png")

######################################
# OUTPUT:                            #
#                                    #
# IMAGE: see challenge_09_output.png #
######################################
