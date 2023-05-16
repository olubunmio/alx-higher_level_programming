#!/usr/bin/python3
"""a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id (you must your PAT instead
as your password)
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    basic_credential = HTTPBasicAuth(argv[1], argv[2])
    req = requests.get(
        'https://api.github.com/user', auth=basic_credential
    )
    print(req.json().get('id'))
    # you can also use
    # req = requests.get(
    #    'https://api.github.com/users/', auth=(argv[1], argv[2])
    # )
