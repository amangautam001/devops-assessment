
#!/bin/bash

set -u

# Validate number of arguments
if [[ $# -gt 1 ]]; then
    echo "Usage: $0 [http://URL or https://URL]"
    exit 2
fi

# Set default URL
URL="${1:-http://localhost:8080/health}"

echo "Health Check Time: $(date)"
echo "Checking URL: $URL"

# Validate URL
if [[ -z "$URL" ]]; then
    echo "ERROR: URL cannot be empty"
    exit 2
fi

if [[ "$URL" != http://* && "$URL" != https://* ]]; then
    echo "ERROR: URL must start with http:// or https://"
    exit 2
fi

# Perform health check
if curl --fail --silent --show-error --max-time 5 "$URL"; then
    echo
    echo "Application is HEALTHY"
    exit 0
else
    echo
    echo "Application is UNHEALTHY"
    exit 1
fi

