#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    y = 0
    while count < x:
        try:
            print("{:d}".format(my_list[count]), end="")
            count += 1
            x += 1
        except (ValueError, TypeError, IndexError):
            pass
        print("")
        return (count)
