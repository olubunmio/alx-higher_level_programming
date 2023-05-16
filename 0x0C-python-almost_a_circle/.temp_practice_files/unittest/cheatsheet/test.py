#!/usr/bin/python3

import unittest

from test_module import TestFoo
from test_module import TestBar
import test_module

def setUpModule():
    print("setUp module")

def tearDownModule():
    print("tearDown module")


if __name__ == "__main__":

    test_module.setUpModule = setUpModule
    test_module.tearDownModule = tearDownModule

    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestFoo)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestBar)

    suite = unittest.TestSuite([suite1, suite2])

    unittest.TextTestRunner(verbosity=2).run(suite)
