# Challenge 2

from collections import Counter

with open("ocr.txt") as f:
    text = f.read()

print("".join(x for x, c in Counter(text).items() if c == 1))

############
# OUTPUT:  #
#          #
# equality #
############
