#!/usr/bin/python3
'''Defines a class MyInt that inherits from int'''


class MyInt(int):
    '''Invert int operators == and !=.'''

    def __eq__(self, data):
        '''Override == opeartor with != behavior.'''
        return self.real != data

    def __ne__(self, data):
        '''Override != operator with == behavior.'''
        return self.real == data
