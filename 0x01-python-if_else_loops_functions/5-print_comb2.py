#!/usr/bin/python3
for c in range(0, 100):
    if c < 99:
        print("{:02}".format(c), end=",")
    else:
        print("{0}".format(c), end="\n")
