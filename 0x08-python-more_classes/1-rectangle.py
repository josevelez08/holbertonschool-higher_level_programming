#!/usr/bin/python3
"""This is module is the base for anothers shapes"""


class Rectangle:
    """shape rectangle, variables such as width high"""
    __width = ""
    __height = ""

    def __init__(self, width=0, height=0):
        self.validateInteger(width, "width")
        self.validateInteger(height, "height")
        self.validate0(width, "width")
        self.validate0(height, "height")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter width"""
        self.validateInteger(value, "width")
        self.validate0(value, "width")
        self.__width = value

    @property
    def height(self):
        """ getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter height"""
        self.validateInteger(value, "height")
        self.validate0(value, "height")
        self.__height = value

    def validateInteger(self, value, name):
        """ module to check that width and height if are integers"""
        try:
            "{:d}".format(value)
        except:
            raise TypeError(name + " must be an integer")

    def validate0(self, value, name):
        """ module to check that width and height if are greater than 0"""
        if value < 0:
            raise ValueError(name + " must be >= 0")
