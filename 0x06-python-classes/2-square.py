#!/usr/bin/python3
"""Square class"""


class Square:
    """ It is the class for define a square: My first class"""
    __size = ''

    def __init__(self, size=0):
        self.__size = size
        try:
            "{:d}".format(size)
            if size < 0:
                raise TypeError
        except(TypeError):
            print("size must be >= 0", end="")
            raise ValueError
        except(ValueError):
            print("size must be an integer", end="")
            raise TypeError
