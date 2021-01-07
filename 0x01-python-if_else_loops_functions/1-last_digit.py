#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > -1:
    ld = number % 10
    if ld == 0:
        print("The last digit of ", number, " is zero")
    elif ld > 5:
        print("The last digit of", number, " is ", ld," and is greater than 5")
    elif ld < 6:
        print("The last digit of", number, " is ", ld, " and is less than 6 and not 0")
else:
    number1 = number * (-1)
    ld = -(number1 % 10)
    print("The last digit of", number, " is ", ld, " and is less than 6 and not 0")
