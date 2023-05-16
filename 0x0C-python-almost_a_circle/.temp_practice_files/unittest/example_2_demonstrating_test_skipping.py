#!/usr/bin/python3
import unittest

## 1-> Method tests can be skipped using the ``skip()`` decorator
class MyTestCase(unittest.TestCase):
    """A class to illusrate method skipping
    """

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        """This function shouldn't count"""
        self.fail("shouldn't happen")

#    @unittest.skipIf(mylib.__version__ < (1, 3), # ``mylib`` is undefined
#                     "not supported in this library version")
#    def test_format(self):
#        """Test that works only for a certain library"""
#        pass
    import sys
    @unittest.skipUnless(sys.platform.startswith('win'),
                          "requires windows")
    def test_windows_supporter(self):
        """Windows specific testing code"""
        pass


## 2-> Classes can also be skipped just like methods

"""A class to illustrate class skipping
"""
@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    """A class to illustrate class skipping
    """

    def test_not_run(self):
        pass
