#!/bin/bash
# sends a GET request to the URL, with a custom header and displays body
curl -sH "X-School-User-Id:98" "${1}"
