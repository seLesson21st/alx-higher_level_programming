#!/usr/bin/python3

if __name__ == "__main__":
    '''Prints the count of a list of arguments'''

    import sys

    total = len(sys.argv) - 1
    if total == 0:
        print("0 arguments.")
    elif total == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(total))
    for x in range(total):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
