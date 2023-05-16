#!/usr/bin/python3
"""Please list 10 commits (from the most recent to oldest) of the repository
passed as the first argument by the user passed as the second argument

You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/

Print all commits by: `<sha>: <author name>` (one by line)
"""
from sys import argv
import requests

if __name__ == "__main__":
    req = requests.get(
        'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    )
    d = req.json()
    count = 10
    for item in d:
        if count == 0:
            break
        print("{}: {}".format(item.get('sha'),
                              item.get('commit').get('author').get('name')))
        count -= 1
