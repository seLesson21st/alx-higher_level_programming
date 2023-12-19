#!/usr/bin/python3

'''Define a square by: (based on 3-square.py)'''


class Square:
    '''represent a square'''
    def __init__(self, size=0):
        '''initializes a square
        Args: size (int): size of the new square
    '''
        self.size = size

        @property
        def size(self):
            return (self.size)

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.size = value

    def area(self):

        '''return area of square'''
        return (self.size * self.size)
