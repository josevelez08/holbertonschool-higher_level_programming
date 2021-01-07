#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > -1:
    ld = number % 10
    if ld == 0:
        print("Last digit of", number, "is", ld, "and is 0")
    elif ld > 5:
        print("Last digit of", number, "is", ld, "and is greater than 5")
    elif ld < 6:
        e = number
        print("Last digit of", e, "is", ld, "and is less than 6 and not 0")
else:
    number1 = number * (-1)
    ld = -(number1 % 10)
    print("Last digit of", number, "is", ld, "and is less than 6 and not 0")
