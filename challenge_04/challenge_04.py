# Challenge 4

import requests
import re


def scan(num):
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    while True:
        text = requests.get(url + num).text
        try:
            num = re.search(r"nothing is (\d+)", text).group(1)
        except:
            return text, num


num = "12345"
message, num = scan(num)
print(f"{message} ({num})")

new_num = int(num) // 2
print(scan(f"{new_num}")[0])

##############################################
# OUTPUT:                                    #
#                                            #
# Yes. Divide by two and keep going. (16044) #
# peak.html                                  #
##############################################
