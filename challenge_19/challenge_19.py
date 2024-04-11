# Challenge 19

import numpy as np
from base64 import b64decode
from scipy.io.wavfile import write

with open("indian.txt") as f:
    data = f.read()
audio = np.frombuffer(b64decode(data), dtype=np.int8)

write("challenge_19_output.wav", 22050, audio)

######################################
# OUTPUT:                            #
#                                    #
# AUDIO: see challenge_19_output.wav #
######################################
