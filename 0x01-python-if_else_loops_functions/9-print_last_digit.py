#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        data = number * (-1)
        ld = data % 10
        print("{:d}".format(ld), end="")
    else:
        ld = number % 10
        print("{:d}".format(ld), end="")
    return ld
