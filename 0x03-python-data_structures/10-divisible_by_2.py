#!/usr/bin/python3
'''function that finds all multiples of 2 in a list.'''


def divisible_by_2(my_list=[]):
    n_list = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            n_list.append(True)
        else:
            n_list.append(False)
            return n_list
