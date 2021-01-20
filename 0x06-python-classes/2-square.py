#!/usr/bin/python3
"""Square class"""


class Square:
    """ It is the class for define a square: My first class"""
    __size = ''

    def __init__(self, size=0):
        self.__size = size
        try:
            if "{:d}".format(size) is False:
                raise TypeError
            if size < 0:
                raise ValueError
        except(TypeError):
            print("size must be >= 0")
        except(ValueError):
            print("size must be an integer")