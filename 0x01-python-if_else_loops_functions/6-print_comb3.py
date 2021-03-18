#!/usr/bin/python3
for j in range(8):
    for t in range(j+1, 10):
        print("{}{}".format(j, t), end=", ")
print("{}{}".format(j+1, t))
