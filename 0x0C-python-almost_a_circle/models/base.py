#!/usr/bin/python3

import json


class Base:
    """ The basic class """
    __nb_objects = 0

    def __init__(self, id=None):
        """Base constructor"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """Json representation of dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
