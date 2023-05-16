#!/usr/bin/python3
"""A module that illustrates ``unittest.TestSuit`` usage.
"""
import unittest

# import test cases from pwd
import example_1
import example_2_demonstrating_test_skipping
import example_3_demonstrating_expected_failure_skipping
import example_4_demonstrating_subset_usage
import example_5_demonstrating_assertions


if __name__ == "__main__":
    x = unittest.TestSuite().__iter__()
    print(list(x))
