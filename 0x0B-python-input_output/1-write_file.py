#!/usr/bin/python3
'''Defines a file writting function'''


def write_file(filename="", text=""):
    '''function that writes a string to a text
    file (UTF8) and returns the number of characters
    written
    Args:
        filename (str)
        text (str)
    Returns:
        number of characters written.
        '''
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
