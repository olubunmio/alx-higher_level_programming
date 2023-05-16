#!/usr/bin/python3
""" a Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as response:
            res = response.read()
    except HTTPError as e:
        print("Error code:", e.code)
    else:
        print(res.decode())
