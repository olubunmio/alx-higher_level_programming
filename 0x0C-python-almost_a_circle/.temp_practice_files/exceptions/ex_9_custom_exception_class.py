#!/usr/bin/python3
"""A module that illustrates how to implement a custom error type.
"""


class DogNameError(Exception):

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)



def get_dog_name():

    dog_name = input("What is your dogName? ")
    if any(char.isdigit() for char in dog_name):
        raise DogNameError("Your dog's name can't contain a number!")
    else:
        return dog_name



if __name__ == "__main__":

    try:
        dog_name = get_dog_name()
    except DogNameError as err:
        print("Error:", err)
