#!/bin/bash
# Get the allowed http methods on a given URL
curl -sIX OPTIONS "${1}" | grep -w 'Allow' | sed 's/Allow: //'
