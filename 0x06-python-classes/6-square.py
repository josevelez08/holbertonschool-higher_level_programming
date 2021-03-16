#!/usr/bin/python3
"""Square class"""


class Square:
    """ It is the class for define a square: My first class"""
    __size = ''
    __position = ''

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        try:
            ("{:d}".format(value))
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        except:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """Position of the square"""
        return self.__position

    @position.setter
    def position(self, position):
        """Set the value"""
        if (type(value) is not tuple) or (len(value) != 2) or\
            type(value[0]) is not int or\
            not isinstance(value[1], int) or\
                (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        size = self.__size
        c = size * size
        return c

    def my_print(self):
        position = self.__position
        size = self.__size
        if size == 0:
            print()
        else:
            for i in range(position[1]):
                print()
            for i in range(size):
                for i in range(size + position[0]):
                    if i < position[0]:
                        print(' ', end="")
                    else:
                        print("#", end="")
                print()
