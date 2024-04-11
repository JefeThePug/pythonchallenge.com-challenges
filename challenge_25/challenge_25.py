# Challenge 25

import io
import wave
import requests
from base64 import b64encode
from PIL import Image

headers = {"Authorization": f"Basic {b64encode(b'butter:fly').decode()}"}
puzzle = []

for i in range(25):
    url = f"http://www.pythonchallenge.com/pc/hex/lake{i + 1}.wav"
    response = requests.get(url, headers=headers)
    puzzle.append(wave.open(io.BytesIO(response.content)))

frames = puzzle[0].getnframes()
output = Image.new("RGB", (300, 300), 0)

for i, wav in enumerate(puzzle):
    byte = wav.readframes(frames)
    img = Image.frombytes("RGB", (60, 60), byte)
    a, b = divmod(i, 5)
    output.paste(img, (60 * b, 60 * a))

output.save("challenge_25_output.png")


######################################
# OUTPUT:                            #
#                                    #
# IMAGE: see challenge_25_output.png #
######################################
