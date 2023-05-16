#!/usr/bin/python3

"""
assertEqual(a, b, msg=None)    -------------> a == b
assertNotEqual(a, b, msg=None) -------------> a != b

assertTrue(x, msg=None)  -------------------> bool(x) is True
assertFalse(x, msg=None)  ------------------> bool(x) is False

assertIs(a, b, msg=None)  ------------------> a is b
assertIsNot(a, b, msg=None)  ---------------> a is not b

assertIsNone(x, msg=None)  -----------------> x is None
assertIsNotNone(x, msg=None)  --------------> x is not None

assertIn(a, b, msg=None)  ------------------> a in b
assertNotIn(a, b, msg=None)  ---------------> a not in b

assertIsInstance(a, b, msg=None)  ----------> isinstance(a, b)
assertNotIsInstance(a, b, msg=None)   ------> not isinstance(a, b)


-> There are also methods used to perform more specific checks, such as:

assertAlmostEqual(a, b, msg=None, delta=None)  -------> round(a-b, 7) == 0
assertNotAlmostEqual(a, b, msg=None, delta=None) -----> round(a-b, 7) != 0

assertGreater(a, b, msg=None)  -----------------------> a > b
assertGreaterEqual(a, b, msg=None)  ------------------> a >= b

assertLess(a, b, msg=None)  --------------------------> a < b
assertLessEqual(a, b, msg=None)  ---------------------> a <= b

assertRegex(text/s, regex/r, msg=None)  --------------> r.search(s)
assertNotRegex(text/s, regex/r, msg=None)  -----------> not r.search(s)

assertCountEqual(a, b, msg=None)  --------------------> a and b have the
                                                        same elements in the
                                                        same number, regard-
                                                        less of their order.

EXCEPTIONS:
-> 1a. assertRaises(exception, callable(function), *args, **kwds)
   1b. assertRaises(exception, msg=None)
      Test that an exception is raised when callable is called with any
      positional or keyword arguments that are also passed to assertRaises()
      The test passes if exception is raised, is an error if another
      exception is raised, or fails if no exception is raised.
      To catch any of a group of exceptions, a tuple containing the
      exception classes may be passed as `exception`.
      Example:
      =======
      self.assertRaises(SomeException, function, arg1, arg2, ...)
      self.assertRaises((Exception1, Exception2, ...), func, arg1, ...)

      If only the exception and possibly the msg arguments are given, return
      a context manager so that the code under test can be written inline
      rather than as a function.
      Example:
      =======
      with self.assertRaises(SomeException):
          do_something(args=None)

      with self.assertRaises(SomeException, mgs="your error message here"):
          do_something(args=None)

      The context manager will store the caught exception object in its
      exception attribute. This can be useful if the intention is to perform
      additional checks on the exception raised.
      Example:
      =======
      with self.assertRaises(SomeException) as cm:
          do_something()

      the_exception = cm.exception
      self.assertEqual(the_exception.error_code, 3)


-> 2a. assertRaisesRegex(exception, regex, callable, *args, *kwds)
   2b. assertRaisesRegex(exception, regex, msg=None)
      Like assertRaises() but also tests that regex matches on the string
      representation of the raised exception. regex may be a regular
      expression object or a string containing a regular expression suitable
      for use by re.search()
      Example:
      =======
      self.assertRaisesRegex(ValueError, "Invalid literal for.*XYZ'$", int,
                             'XYZ')
      OR

      with self.assertRaisesRegex(ValueError, "literal):
          int('XYZ')
          ...


-> 3a. assertWarns(warning, callable, *args, **kwds)
   3b. assertWarns(warning, msg=None)
      Test that a warning is triggered when callable is called with any
      positional or keyword arguments that are also passed to asertWarns().
      The test passes if `warning` is triggered and fails if it isn't. Any
      exception is an error. To catch any of a group of warnings, a tuple
      containing the warning classes may be sassed as `warning`.

      If only the warning and possibly the msg arguments are given, return a
      context manager so that the code under test can be written inline
      rather than as a function:
      Example:
      =======
      self.assertWarns(SomeWarning):
          do_something()

      When used as a context manager, assertWarns() accepts the additional
      keyword argument msg.

      The context manager will store the caught warning object in its
      warning attribute, and the source line which triggered the warnings in
      the filename and lineno attributes. This can be useful if the
      intention is to perform additional checks of the warnings caught.
      Example:
      =======
      with self.assertWarns(SomeWarning) as cm:
          do_something()

      self.assertIn('myfile.py', cm.filename)
      self.assertIn(320, cm.lineno)


-> 4a. assertWarnsRegex(warning, regex, callable, *args, **kwds)
   4b. assertWarnsRegex(warning, regex, msg=None)
      Like assertWarns() but also tests that regex matches on the message of
      the triggered warning. regex may be a regular expression object or a
      string containing a regular expression suitable for use re.search()
      Example:
      =======
      self.assertWarnsRegex(DeprecationWarning,
                            r'legacy_funciton\(\) is deprecated',
                            legacy_function, 'XYZ')

      self.assertWarnsRegex(RuntimeWarning, 'unsafe frobnicating'):
          frobnicate('/etc/passwd')

### I Don't Understand yet
-> 5. assertLogs(logger=None, level=None)
      A context manager to test that at least one message is logged on the
      logger or one of its children, with at least the given level.
"""
