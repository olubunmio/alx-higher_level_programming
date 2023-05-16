#!/usr/bin/python3
"""When sone of your tests differ only by some very small differences, for
instance some parameters, unittest allows you to distinguish them inside the
body of a test method using the subTest() context manager.
"""
import unittest


class NumbersTest(unittest.TestCase):

    def test_even(self):
        """Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(msg=f"Alex test {i+1}", i=i, h=i+1):
                self.assertEqual(i % 2, 0)

        print(help(self.subTest))


# Note:
# ====
# Without using a subtest, execution will stop after the first failure, and
# error would be less easy to diagnose because the value of `i` wouldn't be
# displayed.
