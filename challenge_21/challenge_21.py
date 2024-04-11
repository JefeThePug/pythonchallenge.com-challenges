# Challenge 21

import bz2
import io
import requests
import zipfile
import zlib
from base64 import b64encode

num = 1152983631

auth = f"Basic {b64encode(b'butter:fly').decode()}"
url = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
headers = {"Authorization": auth, "Range": f"bytes={num}-"}
f = requests.get(url, headers=headers)

zip_byte_stream = io.BytesIO(f.content)

with zipfile.ZipFile(zip_byte_stream, "r") as zip_file:
    zip_file.setpassword(b"redavni")
    with zip_file.open(zip_file.infolist()[0], "r") as file:
        print(file.read().decode())

    with zip_file.open(zip_file.infolist()[1], "r") as file:
        data = file.read()
        log = ""

        while True:
            if data.startswith(b"x\x9c"):
                data = zlib.decompress(data)
                log += "."
            elif data.startswith(b"BZh"):
                data = bz2.decompress(data)
                log += "B"
            elif data.endswith(b"\x9cx"):
                data = data[::-1]
                log += "\n"
            else:
                break
        print(data[::-1].decode())

        print(log)

##############################################################################
# OUTPUT:                                                                    #
#                                                                            #
# Yes! This is really level 21 in here.                                      #
# And yes, After you solve it, you'll be in level 22!                        #
#                                                                            #
# Now for the level:                                                         #
#                                                                            #
# * We used to play this game when we were kids                              #
# * When I had no idea what to do, I looked backwards.                       #
#                                                                            #
# look at your logs                                                          #
# ......BBB..........BBB......BBBBBBBB....BBBBBBBB....BBBBBBBBBB..BBBBBBBB   #
# ....BBBBBBB......BBBBBBB....BBBBBBBBB...BBBBBBBBB...BBBBBBBBB...BBBBBBBBB  #
# ...BB.....BB....BB.....BB...BB......BB..BB......BB..BB..........BB......BB #
# ..BB...........BB.......BB..BB......BB..BB......BB..BB..........BB......BB #
# ..BB...........BB.......BB..BBBBBBBBB...BBBBBBBBB...BBBBBBBB....BBBBBBBBB  #
# ..BB...........BB.......BB..BBBBBBBB....BBBBBBBB....BBBBBBBB....BBBBBBBB.  #
# ..BB...........BB.......BB..BB..........BB..........BB..........BB...BB.   #
# ...BB.....BB....BB.....BB...BB..........BB..........BB..........BB....BB.  #
# ....BBBBBBB......BBBBBBB....BB..........BB..........BBBBBBBBB...BB.....BB. #
# ......BBB..........BBB......BB..........BB..........BBBBBBBBBB..BB......BB #
##############################################################################
