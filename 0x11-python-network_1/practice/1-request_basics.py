#!/usr/bin/python3
import requests
"""Behold the power of Requests"""

# Introduction
r = requests.get('https://api.github.com/users/alexUd01', auth=('user', 'pass'))
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())
