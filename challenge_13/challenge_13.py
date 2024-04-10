# Challenge 13

from xmlrpc.client import ServerProxy

conn = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")

evil = "Bert"
result = conn.phone(evil).split("-")[1]

print(result)

###########
# OUTPUT: #
#         #
# ITALY   #
###########
