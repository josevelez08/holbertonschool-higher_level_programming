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
        """ x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter"""
        self.validateInteger(value, "x")
        self.__x = value

    @property
    """ getter y"""
    def y(self):
        return self.__y

    @y.setter
    """setter y"""
    def y(self, y):
        self.validateInteger(y, "y")
        self.__y = y

    @property
    """ getter height"""
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        """setter height"""
        self.validateInteger(height, "height")
        self.validate0(height, "height")
        self.__height = height

    @property
    def width(self):
        """getter width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter width"""
        self.validateInteger(width, "width")
        self.validate0(width, "width")
        self.__width = width

    def validateInteger(self, value, name):
        """validate integer"""
        try:
            "{:d}".format(value)
        except:
            raise TypeError(name + " must be a integer")

    def validate0(self, value, name):
        """validate 0"""
        if value <= 0:
            raise ValueError(name + " must be > 0")

    def validate0xy(self, value, name):
        """ validate 0 in x and y"""
        if value < 0:
            raise ValueError(name + " must be => 0")

    def __init__(self, width, height, x=0, y=0, id=None):
        """ rectangle constructor"""
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
        """ area of rectangle"""
        height = self.__height
        width = self.__width

        return width * height

    def display(self):
        """Print rectangle"""
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
        """Update the data in the class"""
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
        """print to dictionary"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """format the print"""
        return "[Rectangle] ({}) {}/{} - {}/{}".
        format(self.id, self.x, self.y, self.width, self.height)
