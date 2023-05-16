#!/bin/bash
# take in a URL as an argument, send a GET request to the URL
curl -sH "X-School-User-Id: 98" "$1"
