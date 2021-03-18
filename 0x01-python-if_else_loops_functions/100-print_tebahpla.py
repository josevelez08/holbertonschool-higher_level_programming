#!/usr/bin/python3
al = ""
for i in reversed(range(97, 123)):
    if not i % 2:
        al = chr(i).lower()
    else:
        al = chr(i).upper()
    print("{}".format(al), end="")
