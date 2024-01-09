#!/usr/bin/python3
'''defines a text file insertion function.'''


def append_after(filename="", search_string="", new_string=""):
    '''inserts text after each line containing given string in a file.
        Args:
            filename (str)
            search_string (str)
            new_string (str):
    '''
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
