# Challenge 22

from PIL import Image


def draw_dot(i, x, y, size=1):
    for r in range(size):
        for c in range(size):
            i.putpixel((x + r, y + c), 0)


img = Image.open("white.gif")
new = Image.new("RGB", (400, 100), "white")

x, y = -70, 50
for frame in range(img.n_frames):
    img.seek(frame)
    left, top, *_ = img.getbbox()
    left -= 100
    top -= 100
    if left == top == 0:
        x += 80
        y = 50
    x += left
    y += top
    draw_dot(new, x, y, 3)
new.save("challenge_22_output.png")

######################################
# OUTPUT:                            #
#                                    #
# IMAGE: see challenge_22_output.png #
######################################
