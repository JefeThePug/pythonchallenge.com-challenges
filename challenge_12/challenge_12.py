# Challenge 12

from PIL import Image, ImageFile
import io
import os

ImageFile.LOAD_TRUNCATED_IMAGES = True

with open("evil2.gfx", "br") as f:
    data = f.read()
    
images = []
for i in range(5):
    with open(f"{i}.png", "wb") as f:
        f.write(data[i::5])
        try:
            im = Image.open(f"{i}.png")
            images.append(im)
        except:
            print(i)
        else:
            os.remove(f"{i}.png")

width, height = max(img.size for img in images)
combined_image = Image.new("RGB", (width*5, height))

for i, img in enumerate(images):
    combined_image.paste(img, (i * width, 0))

combined_image.save("challenge_12_output.png")

######################################
# OUTPUT:                            #
#                                    #
# IMAGE: see challenge_12_output.png #
######################################
