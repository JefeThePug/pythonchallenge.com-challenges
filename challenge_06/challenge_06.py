# Challenge 6

import zipfile
import re

f = zipfile.ZipFile("channel.zip")
num = "90052"
comments = []
while True:
    content = f.read(f"{num}.txt").decode("utf-8")
    comments.append(f.getinfo(f"{num}.txt").comment.decode("utf-8"))
    try:
        num = re.search("Next nothing is (\d+)", content).group(1)
    except:
        break

f.close()

message = "".join(comments)
print(message)

used = " *\n"
for i in message:
    if i not in used:
        print(i, end="")
        used += i
print()

####################################################################
# OUTPUT:                                                          #
#                                                                  #
# **************************************************************** #
# **************************************************************** #
# **                                                            ** #
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  ** #
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   ** #
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    ** #
# **   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     ** #
# **   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      ** #
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      ** #
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      ** #
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      ** #
# **                                                            ** #
# **************************************************************** #
#  **************************************************************  #
#                                                                  #
# OXYGEN                                                           #
####################################################################
