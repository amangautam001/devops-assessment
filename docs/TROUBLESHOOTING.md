# Troubleshooting Journal – DevOps Assessment

## Issue 1: Nginx Configuration Error

**Symptom:** Nginx configuration test failed.

**Evidence:** `sudo nginx -t` reported `unknown directive "invalid_directive"` at line 84.

**Root Cause:** An intentionally inserted invalid directive in nginx.conf.

**Resolution:** Removed the invalid directive and verified the configuration using `sudo nginx -t`.

**Final Result:** Configuration test successful.

## Issue 2: Favicon HTTP 404

**Symptom:** Browser requested `/favicon.ico` and received HTTP 404.

**Evidence:** Nginx access log recorded `GET /favicon.ico HTTP/1.1` with status `404`.

**Root Cause:** The requested favicon was not available at that path.

**Resolution:** Identified the missing favicon request in the access log. No server failure occurred.

**Final Result:** Main website continued returning HTTP 200.

## Issue 3: Nginx Service Management Verification

**Observation:** Nginx was restarted and its configuration reloaded.

**Evidence:** `systemctl` journal recorded successful stop, start and reload events. `curl -I http://localhost` returned HTTP 200.

**Root Cause:** No service failure occurred; this was a controlled service-management test.

**Resolution:** Verified service status, configuration and HTTP response.

**Final Result:** Nginx remained active and served requests successfully.
## Issue 4: Bash Health Check Connection Failure

**Symptom:** Health-check script reported the application as unhealthy.

**Evidence:** Running the script with http://localhost:9999/health produced curl error 7 and exit code 1.

**Root Cause:** The test used port 9999, where no application was listening.

**Resolution:** Re-ran the script with the correct URL http://localhost:8080/health.

**Final Result:** Health check returned HTTP 200 and exit code 0. The application and database were healthy.
## Issue 5: Nginx Reverse Proxy 502 Bad Gateway

**Symptom:** Requests through Nginx returned HTTP 502 Bad Gateway.

**Evidence:** Nginx error log reported `connect() failed (111: Connection refused)` while connecting to upstream port 5999.

**Root Cause:** The Nginx proxy_pass directive pointed to port 5999 instead of the Flask application's port 5000.

**Resolution:** Restored the correct upstream configuration, tested Nginx syntax and reloaded Nginx.

**Final Result:** The health endpoint returned HTTP 200 and confirmed the database connection.
