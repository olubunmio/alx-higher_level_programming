#!/usr/bin/python3

for i in range(97, 123):
    if i != ord('e') and i != ord('q'):  # if i not in (ord('e'), ord('q'))
        print("{}".format(chr(i)), end='')
