#!/usr/bin/python3
'''function that returns a tuple with the
length of a string and its first character'''


def multiple_returns(sentence):
    the_tuple = ()
    if len(sentence) == 0:
        the_tuple = 0, "None"
    else:
        the_tuple = len(sentence), sentence[0]
        return the_tuple
