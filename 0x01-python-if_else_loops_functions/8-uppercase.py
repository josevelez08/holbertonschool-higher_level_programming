#!/usr/bin/python3
def uppercase(str):
    for i in str:
        g = ord(i)
        if (g >= 97) and (g <= 122):
            g = ord(i) - 32
        print('{:c}'.format(g), end='')
    print()
