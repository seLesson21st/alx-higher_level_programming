#!/usr/bin/python3
""""Prints the ASCII alphabet in lowercase without the letters e an q and a new line."""

for letters in range (97, 123):
    if chr(letters) != 'q'and chr (letters) != 'e':
        print("{}".format(chr(letters)), end ="")
