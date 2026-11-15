#!/bin/bash

set -u

URL="${1:-http://localhost:8080/health}"

echo "Health Check Time: $(date)"
echo "Checking URL: $URL"

if [[ "$URL" != http://* && "$URL" != https://* ]]; then
    echo "ERROR: URL must start with http:// or https://"
    exit 1
fi

if curl --fail --silent --show-error --max-time 5 "$URL"; then
    echo
    echo "Application is HEALTHY"
    exit 0
else
    echo
    echo "Application is UNHEALTHY"
    exit 1
fi
