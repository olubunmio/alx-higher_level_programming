#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for c in str:
        if c >= 'a' and c <= 'z':
            chup = ord(c)
            chup = chup - 32
            chup = chr(chup)
            return upper_str + chup
        else:
            return upper_str + c
