#!/usr/bin/python3
"""A module `base` that contains a class `Base` to be used as the base class
for future implementation of other classes.
"""
import json


class Base:
    """A class that is used as a base class for yet implemented classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):  # Task 1
        """Initializes the class `Base` with `id`.

        Args:
            id(int): the id.
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):  # Task 15
        """A method that returns the JSON string representation of
        ``list_dictionaries``.
        """
        if list_dictionaries is None:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):   # Task 16
        """
        A method that writes the JSON string representation of `list_objs`
        to a file.
        """
        new_list = []
        for item in list_objs:
            if isinstance(item, Base):
                new_list.append(item.to_dictionary())
            else:
                pass   # raise something

        filename = str(cls.__name__) + '.json'

        temp = cls.to_json_string(new_list)

        with open(filename, 'w', encoding='utf-8') as fp:
            fp.write(temp)

    @staticmethod
    def from_json_string(json_string):
        """A method that returns the list of the JSON string representation
        ``json_string``.
        It converts json string to python object.

        Args:
           json_string(str): is a string representing a list of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return json.loads('[]')
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        A method that returns an instance with all attributes already set.
        """
        temp_rect = cls(1, 1)  # dummy values
        temp_rect.update(**dictionary)

        return temp_rect

    @classmethod
    def load_from_file(cls):
        """A method that returns a list of instances.
        """
        filename = cls.__name__ + '.json'

        try:
            with open(filename, 'r', encoding='utf-8') as fp:
                temp = fp.read()
        except FileNotFoundError:
            return []

        temp_list = cls.from_json_string(temp)

        new_list = []
        for item in temp_list:
            new_list.append(cls.create(**item))

        return new_list
