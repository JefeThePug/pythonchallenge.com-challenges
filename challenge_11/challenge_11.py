# Challenge 11

from PIL import Image

image_path = "cave.jpg"

image = Image.open(image_path)
pixels = [*image.getdata()]

new_image = Image.new("RGB", (image.width, image.height // 2))
new_image.putdata(pixels[::2])

new_image.save("challenge_11_output.png")

######################################
# OUTPUT:                            #
#                                    #
# IMAGE: see challenge_11_output.png #
######################################
