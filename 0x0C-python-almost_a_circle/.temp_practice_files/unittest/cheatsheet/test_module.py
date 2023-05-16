#!/usr/bin/python3

import unittest

class TestFoo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("foo setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("foo tearDownClass")


    def setUp(self):
        print("foo setUp")

    def tearDown(self):
        print("foo tearDown")


    def test_foo(self):
        self.assertTrue(True)


class TestBar(unittest.TestCase):
    def setUp(self):
        print("bar setUp")

    def tearDown(self):
        print("bar tearDown")

    def test_bar(self):
        self.assertTrue(True)

