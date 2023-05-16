#!/usr/bin/python3

try:
    raise Exception('spam', "eggs")
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x, y = inst.args  # unpacking .args
    print('x =', x)
    print('y =', y)
    print()
    print(dir(inst))
    print()
    print(inst.with_traceback(None))
