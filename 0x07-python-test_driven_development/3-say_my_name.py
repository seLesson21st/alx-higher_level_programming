#!/usr/bin/python3
'''Defines a name printing function.'''


def say_my_name(first_name, last_name=""):
    '''Prints a name.

     Args:
         first_name (str): name to be print.
         last_name (str): name to be print.
     Raises:
         TypeError: If either of first or last name are not strings.
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
