# Challenge 1

from string import ascii_lowercase as lc

text = (
    "g fmnc wms bgblr rpylqjyrc gr zw fylb. \n"
    "rfyrq ufyr amknsrcpq ypc dmp. \n"
    "bmgle gr gl zw fylb gq glcddgagclr ylb "
    "rfyr'q ufw rfgq rcvr gq qm jmle. \n"
    "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. \n"
    "lmu ynnjw ml rfc spj. \n"
)

table = str.maketrans(lc, lc[2:] + lc[:2])
print(text.translate(table))

# ======================================================================= #

url = "map"
print(url.translate(table))

###########################################################################
# OUTPUT:                                                                 #
#                                                                         #
# i hope you didnt translate it by hand.                                  #
# thats what computers are for.                                           #
# doing it in by hand is inefficient and that's why this text is so long. #
# using string.maketrans() is recommended.                                #
# now apply on the url.                                                   #
#                                                                         #
# ocr                                                                     #
###########################################################################
