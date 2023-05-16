#!/usr/bin/python3
"""A module that contains a class `Square` that inherits from a class
`Rectangle`.
"""
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """A getter and setter method that for size."""
        return self.__width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """A method that assigns values to object attributes.
        """
        if args and len(args) != 0:
            if len(args) == 1:  # only one argument passed
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]
            elif len(args) > 4:
                pass  # TODO: raise something/do something

        elif kwargs and len(kwargs) != 0:
            lst = ['id', 'size', 'x', 'y']
            for item in kwargs:
                if item not in lst:
                    raise KeyError("TODO: Not implemented yet")
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.width = kwargs['size']
                self.height = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

        else:
            pass  # TODO: Implement later

    def to_dictionary(self):
        """A method that returns a dictionary containing the attributes of a
        square object and their respective values.
        """
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
