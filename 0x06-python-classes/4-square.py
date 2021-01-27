#!/usr/bin/python3
"""Square class"""


class Square:
    """ It is the class for define a square: My first class"""
    __size = ''

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        try:
            ("{:d}".format(value))
            self.__size = value
        except:
            raise TypeError("size must be an integer")

    def area(self):
        size = self.__size
        c = size * size
        return c
