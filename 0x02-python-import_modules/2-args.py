#!/usr/bin/python3
import sys

if __name__ == "__main__":
    count = 0
    size = len(sys.argv)
    print("{} argunmets:".format(size - 1))
    for i in sys.argv[1:]:
        count += 1
        print("{}: {}".format(count, i))
