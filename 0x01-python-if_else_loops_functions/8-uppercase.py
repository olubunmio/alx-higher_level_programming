#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for c in str:
        if c >= 'a' and c <= 'z':
            chup = ord(c)
            chup = chup - 32
            chup = chr(chup)
            upper_str = upper_str + chup
        else:
            upper_str = upper_str + c
    print("{}".format(upper_str))
