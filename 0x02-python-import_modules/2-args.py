#!/usr/bin/python3

import sys

if __name__ == "__main__":
    count = 0
    if len(sys.argv) == 1:
        print("{} arguments.".format(len(sys.argv) - 1))
    elif len(sys.argv) == 2:
        print("{} argument:".format(len(sys.argv) - 1))
        print("{}: {}".format(len(sys.argv) - 1, sys.argv[1]))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i in sys.argv[1:]:
            count += 1
            print("{}: {}".format(count, i))
