#!/usr/bin/python3
import sys

if __name__ == "__main__":
    count = 0
    size = len(sys.argv) - 1
    if size == 0:
        print("0 arguments.")
    elif size == 1:
        print("{} argument:".format(size))
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format(size))
        for i in sys.argv[1:]:
            count += 1
            print("{}: {}".format(count, i))
