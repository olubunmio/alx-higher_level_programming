#!/usr/bin/python3
""" A module that illustrates:

1. setUpModule and tearDownModule
2. setUpClass and tearDownClass
3. setUp and tearDown
"""
import unittest


def setUpModule():
    print("Setup module")

def tearDownModule():
    print("Tear Down Module")


def fib(n):
    return 1 if n <= 2 else fib(n-1) + fib(n-2)


class TestFib(unittest.TestCase):
    """A class that illustrates setUpClass and TearDownClass.
    """
    @classmethod
    def setUpClass(cls):
        print("Setup class")

    @classmethod
    def tearDownClass(cls):
        print("Tear down class")


    def setUp(self):
        print("setup")
        self.n = 10

    def tearDown(self):
        print("Tear Down")
        del self.n


    def test_fib_1(self):
        self.assertEqual(fib(self.n), 55)

    def test_fib_2(self):
        self.assertTrue(fib(self.n) == 55)


if __name__ == "__main__":
    unittest.main()
