# Challenge 23

import codecs
import io
import re
from contextlib import redirect_stdout

buffer = io.StringIO()

with redirect_stdout(buffer):
    import this
buffer.seek(0)
zen = buffer.read()

print(zen)

s = "va gur snpr bs jung?"
print(codecs.decode(s, "rot-13"))

match = re.search(r"(?:in the face of )(\w+)(?:\W)", zen, re.IGNORECASE)

print(match.group(1))

#########################################################################
# OUTPUT:                                                               #
#                                                                       #
# The Zen of Python, by Tim Peters                                      #
#                                                                       #
# Beautiful is better than ugly.                                        #
# Explicit is better than implicit.                                     #
# Simple is better than complex.                                        #
# Complex is better than complicated.                                   #
# Flat is better than nested.                                           #
# Sparse is better than dense.                                          #
# Readability counts.                                                   #
# Special cases aren't special enough to break the rules.               #
# Although practicality beats purity.                                   #
# Errors should never pass silently.                                    #
# Unless explicitly silenced.                                           #
# In the face of ambiguity, refuse the temptation to guess.             #
# There should be one-- and preferably only one --obvious way to do it. #
# Although that way may not be obvious at first unless you're Dutch.    #
# Now is better than never.                                             #
# Although never is often better than *right* now.                      #
# If the implementation is hard to explain, it's a bad idea.            #
# If the implementation is easy to explain, it may be a good idea.      #
# Namespaces are one honking great idea -- let's do more of those!      #
#                                                                       #
# in the face of what?                                                  #
# ambiguity                                                             #
#########################################################################
