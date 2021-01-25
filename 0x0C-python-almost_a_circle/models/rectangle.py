#!/usr/bin/python3


class Base:
    """The basic class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id


class Rectangle (Base):
    """The rectangle class """
    __width = ''
    __height = ''
    __x = ''
    __y = ''
    # getter methods

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get__height(self):
        return self.__height

    def get_width(self):
        return self.__width

    # setter methods
    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
