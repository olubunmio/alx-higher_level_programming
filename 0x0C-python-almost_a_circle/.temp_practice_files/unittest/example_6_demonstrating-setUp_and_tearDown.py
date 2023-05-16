#!/usr/bin/python3
""" A module that illustrates:

1. setUpModule and tearDownModule
2. setUpClass and tearDownClass
3. setUp and tearDown
"""
import unittest

# 1. module
def setUpModule():
    createconnection():
    # if an exception is raised in a `setUpModule` then none of the tests in
    # the module will be run and the `tearDownModule` will not be run.

def tearDownModule():
    closeConnection()


# 2. class
class Test(unittest.TestCase):
    """A class that illustrates setUpClass and TearDownClass.
    """
    @classmethod
    def setUpClass(cls):
        cls._connection = createExpensiveConnectionObject()

    @classmethod
    def tearDownClass(cls):
        cls._connection.destroy()
