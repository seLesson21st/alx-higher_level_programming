#!/usr/bin/python3
'''
function that returns the list of available
attributes and methods of an object
'''


def lookup(obj):
    '''
    This function returns a list of available attributes .
    '''

    return dir(obj)
