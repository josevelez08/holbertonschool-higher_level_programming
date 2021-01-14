#!/usr/bin/python3
import sys

if __name__ == "__main__":
    count = 0
    size = len(sys.argv) - 1
    if size == 1:
        print("{} argunmet:".format(size))
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} argunmets:".format(size))
        for i in sys.argv[1:]:
            count += 1
            print("{}: {}".format(count, i))
