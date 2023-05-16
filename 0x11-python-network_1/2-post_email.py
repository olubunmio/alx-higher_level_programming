#!/usr/bin/python3
"""A python script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter and displays the body of the
response
"""
from urllib.request import urlopen
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    q = {'email': argv[2]}
    q = urlencode(q)
    data = q.encode('ascii')
    with urlopen(argv[1], data=data) as response:
        res = response.read()
        print(res.decode('utf8'))
