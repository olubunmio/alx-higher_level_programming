#!/bin/bash
# take in a URL, sends a POST request to the passed URL
curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" -X POST "$1"
