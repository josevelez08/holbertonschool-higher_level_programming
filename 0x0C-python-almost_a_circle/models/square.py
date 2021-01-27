#!/usr/bin/python3
from models.rectangle import Rectangle
"""Square flie"""


class Square(Rectangle):

    """class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super(Square, self).__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".
        format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        dic = ["id", "size", "x", "y"]
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
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
