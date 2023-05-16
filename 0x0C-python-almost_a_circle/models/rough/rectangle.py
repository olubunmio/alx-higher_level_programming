#!/usr/bin/python3
"""A module that contains a class `Rectangle` that inherits from Base.
"""
from models.base import Base


class Rectangle(Base):
    """A class that inherits from a base class `Base`.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes private instance attributes as follows.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter and setter method for `width` instance attribute.
        """
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:  # or use `not isinstance(width, int)`
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Getter and setter method for `height` instance attribute."""
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Getter and setter methods for `x` attribute.
        """
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Getter and setter methods for `y` instance attribute.
        """
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):  # Task 4:
        """
        A method that computes and returns the area of a rectangle object.
        """
        return self.__width * self.__height

    def display(self):  # Task 5: create Task 7: Update (implement x & y)
        """
        A method that prints in stdout the rectangle object with `#`.
        """
        print('\n' * self.__y, end='')      # handle y-axis
        for i in range(self.__height):
            print(' ' * self.__x, end='')   # handle x-axis
            print('#' * self.__width)

    def __str__(self):  # Task 6:
        """return formated string."""
        args = (type(self).__name__, self.id, self.__x, self.__y,
                self.__width, self.__height)
        return "[{}] ({}) {}/{} - {}/{}".format(*args)

    def update(self, *args, **kwargs):
        """A method that assigns new values to the instance attributes.
        #-> Task 8: create `def(self, *args)`
        #-> Task 9: update to `def(self, *args,  **kwargs)`.
        """
        if args and len(args) != 0:  # Case 1: args is not empty
            # handle args
            if len(args) == 1:  # only one argument passed
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.__width = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
            elif len(args) >= 5:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            elif len(args) > 5:  # redundant
                pass

        elif kwargs and len(kwargs) != 0:   # Case 2: args is empty
            lst = ['id', 'width', 'height', 'x', 'y']
            for item in kwargs:
                if item not in lst:
                    raise KeyError("{} not in found".format(item))
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

        else:
            pass  # TODO: Implement something later

    def to_dictionary(self):
        """A method that returns a dictionary containing the attributes of a
        rectangle object and their respective values.
        """
        return {'id': self.id, 'width': self.__width,
                'height': self.__height, 'x': self.__x, 'y': self.__y}
