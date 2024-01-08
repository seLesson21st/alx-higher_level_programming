#!/usr/bin/python3
'''Defines an subclass or child list class MyList.'''


class MyList(list):
    '''This is a subclass of the built-in list class.'''

    def print_sorted(self):
        '''prints a sorted list in an ascending order.'''
        print(sorted(self))
