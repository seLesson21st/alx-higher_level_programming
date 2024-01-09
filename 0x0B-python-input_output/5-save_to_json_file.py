#!/usr/bin/python3
'''Defines a json file writing function'''
import json


def save_to_json_file(my_obj, filename):
    '''function that writes an Object to
    a text file, using a JSON representation'''
    with open(filename, "w") as f:
        json.dump(my_obj, f)
