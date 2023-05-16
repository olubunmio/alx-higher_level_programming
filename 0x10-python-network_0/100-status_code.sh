#!/bin/bash
# a bash script that sends a request to a url passed as an argument and displays the status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
