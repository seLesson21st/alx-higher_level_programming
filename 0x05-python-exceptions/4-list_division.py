#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    updated = []
    for x in range(0, list_length):
        try:
            divide = my_list_1[x] / my_list_2[x]
        except TypeError:
            print("wrong type")
            divide = 0
        except ZeroDivisionError:
            print("dividion by 0")
            divide = 0
        finally:
            updated.append(divide)
        return (updated)
