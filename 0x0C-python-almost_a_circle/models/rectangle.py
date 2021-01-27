#!/usr/bin/python3
from models.base import Base
""" Rentangle file """


class Rectangle (Base):
    """" Class Rectangle """

    __width = ''
    __height = ''
    __x = ''
    __y = ''

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validateInteger(value, "x")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.validateInteger(y, "y")
        self.__y = y

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.validateInteger(height, "height")
        self.validate0(height, "height")
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.validateInteger(width, "width")
        self.validate0(width, "width")
        self.__width = width

    def validateInteger(self, value, name):
        try:
            "{:d}".format(value)
        except:
            raise TypeError(name + " must be a integer")

    def validate0(self, value, name):
        if value <= 0:
            raise ValueError(name + " must be > 0")

    def validate0xy(self, value, name):
        if value < 0:
            raise ValueError(name + " must be => 0")

    def __init__(self, width, height, x=0, y=0, id=None):
        self.validateInteger(width, "width")
        self.validateInteger(height, "height")
        self.validateInteger(x, "x")
        self.validateInteger(y, "y")
        self.validate0(width, "width")
        self.validate0(height, "height")
        self.validate0xy(x, "x")
        self.validate0xy(y, "y")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def area(self):
        height = self.__height
        width = self.__width

        return width * height

    def display(self):
        height = self.__height
        width = self.__width
        x = self.__x
        y = self.__y
        for coordinatesY in range(y):
            print("")
        for h in range(height):
            for w in range(width):
                if w == 0:
                    for coordinatesX in range(x):
                        print(" ", end="")
                print('#', end="")
            print("")

    def update(self, *args, **kwargs):
        dic = ["id", "height", "width", "x", "y"]
        if len(args) != 0:
            for i in range(len(args)):
                setattr(self, dic[i], args[i])
        else:
            for i in range(len(dic)):
                try:
                    setattr(self, dic[i], kwargs[dic[i]])
                except:
                    continue

    def to_dictionary(self):
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".
        format(self.id, self.x, self.y, self.width, self.height)
