#!/usr/bin/python3
import unittest

# Expected failures can be skipped using the ``expectedFailure()`` decorator

class ExpectedFailureTestCase(unittest.TestCase):
    """A class that demonstrates expectedFailure() decorator usage
    """

    @unittest.expectedFailure
    def test_not_run(self):
        pass


## CREATING CUSTOM DECORATORS
#
# def skipUnlessHasattr(obj, attr):
#     if hasattr(obj, attr):
#         return lambda func: func
#     return unittest.skip("{!r} doesn't have {!r}".format(obj, attr))


# What is `!r`?
if __name__ == "__main__":
    print("{!r} is {!r}".format(ExpectedFailureTestCase, 'udo'))


# The following decorators implement test skipping and expected failures:
#
# 1. @unittest.skip("reason")  -  Unconditionally skip the decorated test.
#    "reason" should describe why the test is being skipped.
#
# 2. @unittest.skipIf(condition, "reason")  -  Skip the decorated test if
#    `condition` is true.
#
# 3. @unittest.skipUnless(condition, "reason")  -  Skip the decorated test
#    unless `condition` is true.
#
# 4. @unittest.expectedFailure  -  Mark the test as an expected failure. If
#    the test fails when run, the test is not counted as a failure.
#
# 5. exception unittest.skipTest("reason")  -  This `exception` is raised to
#    skip a test.
#    Usually you can use TestCase.skipTest() or one of the skipping
#    decorators instead of raising this directly.
#
# NOTE:
# ====
# -> Skipped tests will not have setUp() or tearDown() run around them.
# -> Skipped classes will not have setUpClass() or tearDownClass() run.
# -> Skipped modules will not have setUpModule() or tearDownModule() run.
#

