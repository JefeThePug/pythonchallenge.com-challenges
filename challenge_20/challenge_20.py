# Challenge 20

import bz2
import re
import requests
from base64 import b64encode

auth = f"Basic {b64encode(b'butter:fly').decode()}"
url = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
headers = {"Authorization": auth}
f = requests.get(url, headers=headers)

p = re.compile("bytes (\d+)-(\d+)/(\d+)")
while True:
    try:
        s, e, l = p.search(f.headers["content-range"]).groups()
        headers["Range"] = f"bytes={int(e) + 1}-"
        f = requests.get(url, headers=headers)
        print(f.text)
    except KeyError:
        break

headers["Range"] = f"bytes={l}-"
f = requests.get(url, headers=headers)
print(f.text[::-1])

s = p.search(f.headers["content-range"]).group(1)
headers["Range"] = f"bytes={int(s) - 1}-"
f = requests.get(url, headers=headers)
print(f.text)

##################################################
# OUTPUT:                                        #
#                                                #
# Why don't you respect my privacy?              #
#                                                #
# we can go on in this way for really long time. #
#                                                #
# stop this!                                     #
#                                                #
# invader! invader!                              #
#                                                #
# ok, invader. you are inside now.               #
#                                                #
#                                                #
#                                                #
# the password is your new nickname in reverse   #
# and it is hiding at 1152983631.                #
##################################################
