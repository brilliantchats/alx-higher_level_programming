#!/bin/bash
# sends a GET request to the URL, with a custom header and displays body
curl -s -X GET -H "X-School-User-Id: 98" "${1}"
