#!/usr/bin/python3
"""All assert methods accept a `msg` argument that, if specified, is used as
the error message on failure.
"""
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper(), msg="not upper")

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)



if __name__ == "__main__":
    unittest.main()
