# Challenge 14

from PIL import Image

w = 100
img = Image.open("wire.png")
result = Image.new("RGB", (w, w), "white")
pixels = [*img.getdata()]

i = 0
while pixels:
    for y in range((i+3)//4, (w-1)-(i+1)//4 + 1):
        result.putpixel((i//4, y), pixels.pop(0))
    i += 1
    result = result.rotate(-90)
    
result = result.rotate(180).resize((500,500))

result.save("challenge_14_output.png")

######################################
# OUTPUT:                            #
#                                    #
# IMAGE: see challenge_14_output.png #
######################################
