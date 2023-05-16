#!/usr/bin/python3
"""Exception chaining using ``from <ExceptionName>``
"""

def func():
    raise ConnectionError


if __name__ == "__main__":
    try:
        func()
    except ConnectionError as err:
        raise RuntimeError("Could not open database") from err
