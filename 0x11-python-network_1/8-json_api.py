#!/usr/bin/python3
""" a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv

if __name__ == "__main__":
    val = argv[1] if len(argv) > 1 else ""
    req = requests.post("http://0.0.0.0:5000/search_user", data={'q': val})

    try:
        result = req.json()
    except Exception:
        print("Not a valid JSON")
    else:
        if len(result):
            print("[{}] {}".format(result['id'], result['name']))
        else:
            print("No result")
