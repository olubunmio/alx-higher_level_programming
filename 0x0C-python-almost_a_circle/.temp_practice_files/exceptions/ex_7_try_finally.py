#!/usr/bin/python3
"""
->If an exception occurs during execution during execution of the try clause,
  the exception may be handled by an except clause. If the exception is not
  handled by an except clause, the exception is re-raised after the finally
  clause has been executed.

->An exception could occur during execution of an except or else clause.
  Again, the exception is re-raised after the finally clause has been
  executed.

->If the finally clause executes a `break`, `continue`, or `return`statement,
  exceptions are not re-raised.

->If the try statement reaches a `break`, `continue`, or `return` statement,
  the finally clause will execute just prior to the break, continue or
  return statement's execution.

->If a finally clause includes a return statement, the returned value will
  be the one from the finally clause's return statement, not the value from
  the try clause's return statement.
Examples:
========
"""
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


def bool_return():
    try:
        return True
    finally:
        return False


if __name__ == "__main__":
    print(bool_return())
    print()
    divide(2, 1)
    print()
    divide(2, 0)
    print()
    divide("2", "1")
