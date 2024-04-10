# Challenge 10

from itertools import pairwise


def look_and_say(n):
    if n < 3:
        return "1" * n

    s = "11"
    for _ in range(n - 2):
        s += "#"
        c = 1
        tmp = ""

        for a, b in pairwise(s):
            if b != a:
                tmp += f"{c + 0}"
                tmp += a
                c = 1
            else:
                c += 1
        s = tmp
    return s


N = 31
sequence = look_and_say(N)
print(len(sequence))

###########
# OUTPUT: #
#         #
# 5808    #
###########
