#!/usr/bin/python3
"""Square class"""


class Square:
    """ It is the class for define a square: My first class"""
    __size = ''

    def __init__(self, size=0):
        try:
            self.__size = "{:d}".format(size)
        except(TypeError):
            print("size must be an integer")
        except(ValueError):
            print("size must be >= 0")
