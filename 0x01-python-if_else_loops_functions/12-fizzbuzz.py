#!/usr/bin/python3
"""print Fizz instead of the number and for multiples of five print Buzz
 numbers which are multiples of both three and five print FizzBuzz"""


def fizzbuzz():
    for numbers in range(1, 101):
        if numbers % 3 == 0 and numbers % 5 == 0:
            print("Fizzbuzz ", end="")
        elif numbers % 3 == 0:
            print("Fizz ", end="")
        elif numbers % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(numbers), end="")
