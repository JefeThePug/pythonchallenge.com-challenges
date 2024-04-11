# Challenge 18

import gzip
from difflib import Differ
from contextlib import ExitStack
from PIL import Image

with gzip.open("deltas.gz", "rb") as f:
    left, right = [], []
    for line in f:
        left.append(line[:53].decode())
        right.append(line[56:-1].decode())

file_paths = ["equal.png", "minus.png", "plus.png"]

with ExitStack() as stack:
    files = [stack.enter_context(open(file_path, "wb")) for file_path in file_paths]

    for row in Differ().compare(left, right):
        data = bytes([int(i, 16) for i in row[2:].strip().split() if i])
        files[" -+".find(row[0])].write(data)

images = [Image.open(f"{x}.png") for x in ("plus", "minus", "equal")]
height = max(i.height for i in images)
widths = [i.width for i in images]
combined_image = Image.new("RGB", (sum(widths), height))

for i, img in enumerate(images):
    combined_image.paste(img, (i * widths[max(0, i - 1)], 0))

combined_image.save("challenge_18_output.png")

######################################
# OUTPUT:                            #
#                                    #
# IMAGE: see challenge_18_output.png #
######################################
