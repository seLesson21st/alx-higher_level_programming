#!/usr/bin/python3


for c in range(ord('z'), ord('a') -1, -1):
    if c % 2 == 0:
        x = 0
    else:
        x = 32
    print("{}".format(chr(c - x)), end="")
