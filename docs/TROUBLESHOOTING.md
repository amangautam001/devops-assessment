# Troubleshooting Journal – DevOps Assessment

## Issue 1: Nginx Configuration Error

**Symptom:** Nginx configuration test failed.

**Hypothesis:** An invalid directive might have been added to the configuration file.

**Evidence and Commands:**
- `sudo nginx -t`
- `sudo journalctl -u nginx --no-pager -n 30`

The configuration test reported `unknown directive "invalid_directive"` at line 84.

**Root Cause:** An intentionally inserted invalid directive in the Nginx configuration.

**Resolution:** Removed the invalid directive and ran `sudo nginx -t` again. Reloaded Nginx after successful validation.

**Final Result:** Nginx configuration test passed and the service operated normally.

## Issue 2: Favicon HTTP 404

**Symptom:** Browser requested `/favicon.ico` and received HTTP 404.

**Hypothesis:** The favicon file might be missing from the requested path.

**Evidence and Commands:**
- `sudo tail -n 30 /var/log/nginx/access.log`
- `curl -I http://localhost/favicon.ico`

The access log recorded a GET request for `/favicon.ico` with status 404.

**Root Cause:** The requested favicon was not available at that path.

**Resolution:** Identified the missing favicon request in the access log. No server configuration change was necessary.

**Final Result:** The main website continued returning HTTP 200. The favicon 404 did not affect the main service.

## Issue 3: Nginx Service Management Verification

**Observation:** Nginx was restarted and its configuration reloaded as part of service-management verification.

**Hypothesis:** The service should remain active and serve requests after a controlled restart and reload.

**Evidence and Commands:**
- `sudo systemctl status nginx`
- `sudo systemctl restart nginx`
- `sudo systemctl reload nginx`
- `sudo journalctl -u nginx --no-pager -n 30`
- `curl -I http://localhost`

**Root Cause:** No service failure occurred. This was a controlled service-management test.

**Resolution:** Verified service status, configuration and HTTP response after restart and reload.

**Final Result:** Nginx remained active and returned HTTP 200.

## Issue 4: Bash Health Check Connection Failure

**Symptom:** The health-check script reported the application as unhealthy.

**Hypothesis:** The application might not be listening on the requested port.

**Evidence and Commands:**
- `./scripts/health-check.sh http://localhost:9999/health`
- `echo $?`
- `./scripts/health-check.sh http://localhost:8080/health`

The incorrect port produced curl error 7 and exit code 1.

**Root Cause:** No application was listening on port 9999.

**Resolution:** Re-ran the health-check script using the correct application endpoint on port 8080.

**Final Result:** The health check returned HTTP 200 and exit code 0. The application and database were healthy.

## Issue 5: Nginx Reverse Proxy 502 Bad Gateway

**Symptom:** Requests through Nginx returned HTTP 502 Bad Gateway.

**Hypothesis:** Nginx might be forwarding requests to an incorrect upstream port.

**Evidence and Commands:**
- `curl -i http://localhost:8080/health`
- `docker compose logs --tail=50 nginx`
- `docker compose logs --tail=50 app`
- `grep -n "proxy_pass" nginx/nginx.conf`

The Docker Nginx error log reported `connect() failed (111: Connection refused)` while connecting to upstream port 5999.

The Nginx configuration showed that the upstream port did not match the Flask application's listening port 5000.

**Root Cause:** The `proxy_pass` directive pointed to port 5999 instead of the Flask application's port 5000.

**Resolution:** Restored the correct upstream configuration, tested Nginx syntax and reloaded Nginx.

**Final Result:** The health endpoint returned HTTP 200 and confirmed the database connection.
