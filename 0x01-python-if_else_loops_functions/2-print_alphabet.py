#!/usr/bin/python3
""""Prints the ASCII alphabet in lowercase without a new line."""

for letters in range(97, 123):
    print("{}".format(chr(letters)), end="")
