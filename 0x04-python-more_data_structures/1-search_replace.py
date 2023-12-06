#!usr/bin/python3
'''function that replaces all occurrences of an
element by another in a new list'''


def search_replace(my_list, search, replace):
    if len(my_list) == 0:
        return n_list
    n_list = [content if content != search else replace for content in my_list]
    return n_list
