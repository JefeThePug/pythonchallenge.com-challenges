# Challenge 17

import re
import requests
from bz2 import decompress
from xmlrpc.client import ServerProxy
from urllib.parse import unquote_to_bytes
from base64 import b64encode
from bs4 import BeautifulSoup

MAIN = "http://www.pythonchallenge.com/pc/"


def scan(num):
    url = f"{MAIN}def/linkedlist.php?busynothing="
    cookies = ""
    while True:
        f = requests.get(url + num)
        text = f.text
        cookies += f.cookies.get_dict()["info"]
        try:
            num = re.search(r"nothing is (\d+)", text).group(1)
        except:
            return cookies


num = "12345"
cookies = unquote_to_bytes(scan(num).replace("+", " "))

print(decompress(cookies).decode("utf-8"))

conn = ServerProxy(f"{MAIN}/phonebook.php")

father = "Leopold"
result = conn.phone(father).split("-")[1].lower()

print(result)

url = f"{MAIN}return/{result}.html"
auth = f"Basic {b64encode('huge:file'.encode()).decode()}"
f = requests.get(url, headers={"Authorization": auth})

url = f"{MAIN}{f.text.split('..')[1][1:-2]}"
cookies = {"info": "the flowers are on their way"}

f = requests.get(url, headers={"Authorization": auth}, cookies=cookies)
answer = BeautifulSoup(f.text, "html.parser").body.get_text()

print(answer.strip().split()[-1][:-1])


#################################################################################################################
# OUTPUT:                                                                                                       #
#                                                                                                               #
# is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand. #
# violin                                                                                                        #
# balloons                                                                                                      #
#################################################################################################################
