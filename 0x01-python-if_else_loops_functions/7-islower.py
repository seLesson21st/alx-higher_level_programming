#!/usr/bin/python3
"""Function that checks for lower case characters"""

def islower(c):

    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
