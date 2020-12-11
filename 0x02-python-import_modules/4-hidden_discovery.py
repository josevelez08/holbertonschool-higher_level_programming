#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    for defined in dir():
        if defined[1] != "_":
            print(defined)
