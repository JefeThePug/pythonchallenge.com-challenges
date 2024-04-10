# Challenge 3

import re

with open("equality.txt") as f:
    text = f.read()

print("".join(re.findall(r"(?<![A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?![A-Z])", text)))

##############
# OUTPUT:    #
#            #
# linkedlist #
##############
