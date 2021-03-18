#!/usr/bin/python3
alt = ""
for i in reversed(range(97, 123)):
    if not i % 2:
        alt = chr(i).lower()
    else:
        alt = chr(i).upper()
    print("{}".format(alt), end="")
