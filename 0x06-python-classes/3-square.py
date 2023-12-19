#!/usr/bin/python3

'''Define a square by: (based on 2-square.py)'''


class Square:
    '''represent a square'''
    def __init__(self, size=0):
        '''initializes a square
        Args: size (int): size of thr new square
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        '''Return the current arear of square'''
        return (self.__size * self.__size)
