#!/usr/bin/python3
'''Defines a function that adds attributes to objs.'''


def add_attribute(obj, attr, data):
    '''Add a new attribute to an object if possible.

        Args:
            obj (any): to be add an attribute to.
            attr (str): attribute to add to obj.
            value (any): The value of att.
        Raises:
            TypeError: If the attribute cannot be added.
    '''
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, data)
