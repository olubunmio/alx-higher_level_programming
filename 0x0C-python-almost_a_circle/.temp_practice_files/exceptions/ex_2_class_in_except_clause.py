#!/usr/bin/python3

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass


if __name__ == "__main__":

    for item in [B, C, D]:
        try:
            raise item(f"{item.__name__} raised")
        except D:
            print("D")
        except C:
            print("C")
        except B:
            print("B")
