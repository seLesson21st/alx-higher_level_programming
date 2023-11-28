#!/usr/bin/python3
""" prints all possible different combinations of two digits"""

for numbers in range(0, 100):
    if numbers == 99:
        print("{}".format(numbers))
    else:
        print("{:02}".format(numbers), end=", ")
