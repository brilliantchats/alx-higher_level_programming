#!/usr/bin/bash
# Displays the size of the body of the response from a GET request on a URL
curl -sI "${1}" | grep 'Content-Length' | sed 's/.* //'
