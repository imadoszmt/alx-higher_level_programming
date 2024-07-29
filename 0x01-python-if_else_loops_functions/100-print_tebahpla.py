#!/usr/bin/python3

for alphabet in range(26):
    if alphabet % 2 == 0:
        print("{}".format(chr(122 - alphabet)), end="")
    else:
        print("{}".format(chr(90 - alphabet)), end="")
