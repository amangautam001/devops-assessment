# Learning Reflection – DevOps Assessment

## 1. Introduction

During this assessment, I worked on building and running a containerized Student Management API using Linux, Python, Docker, PostgreSQL, Nginx and GitHub Actions.

The main objective was to understand how different DevOps components work together in a practical environment.

## 2. What I Learned

### Linux Administration
- Working with Ubuntu through WSL2.
- Managing users, directories and file permissions.
- Checking running processes, memory, disk usage and network ports.
- Managing the Nginx service.
- Testing and troubleshooting Nginx configuration.

### Networking and Nginx
- Understanding localhost, IP addresses, DNS and TCP ports.
- Using curl to test HTTP responses.
- Configuring Nginx as a reverse proxy.
- Understanding HTTP status codes such as 200, 404 and 502.
- Identifying incorrect upstream configuration.

### Docker and Docker Compose
- Creating a Dockerfile for a Flask application.
- Running multiple services using Docker Compose.
- Understanding container networking.
- Using health checks and environment variables.
- Running the application as a non-root user.
- Using Docker volumes to preserve database data.

### Git and GitHub Actions
- Creating a Git repository and pushing code to GitHub.
- Working with branches and pull requests.
- Creating an automated CI workflow.
- Running Python tests and building a Docker image.
- Understanding how CI detects failed tests and verifies corrections.

### Bash Scripting
- Creating a health-check script.
- Checking HTTP endpoint availability.
- Returning appropriate exit codes for success and failure.

## 3. Challenges Faced

Some of the important issues encountered during this assessment were:

1. An invalid Nginx directive caused configuration validation to fail.
2. An incorrect Nginx upstream port caused HTTP 502 errors.
3. A health-check request to an unavailable port returned a connection error.
4. An intentionally incorrect test assertion caused GitHub Actions to fail.

I investigated the errors using configuration tests, logs, curl and pytest, then corrected the relevant configuration or test.

More details are recorded in `docs/TROUBLESHOOTING.md`.

## 4. Key Learnings

I learned that successful application deployment requires more than writing application code. Networking, service configuration, database connectivity, container health, permissions and automation are also important.

I also learned that logs and error messages are essential for identifying the actual root cause instead of guessing.

## 5. Areas for Improvement

I want to improve my knowledge of:
- Advanced Linux administration.
- Python and Flask development.
- Docker networking and security.
- CI/CD pipeline design.
- Automated integration testing.
- Production monitoring and deployment.

## 6. Resources Used

The following resources and tools were used during the assessment:

- Official Docker documentation for Dockerfile and Docker Compose concepts.
- Official Nginx documentation for reverse proxy configuration.
- Official Flask documentation for API development.
- Official PostgreSQL documentation for database operations and backups.
- GitHub Actions documentation for CI workflow configuration.
- Linux manual pages and terminal help for Linux commands.

AI assistance was used to understand concepts, troubleshoot errors, review commands and improve documentation. I executed and verified the relevant commands in my local environment.

## 6. Conclusion

This assessment provided practical exposure to several DevOps tools and workflows. It helped me understand how an application moves from local development to a containerized environment and how automated testing can detect problems before code is merged.

AI assistance was used during learning and troubleshooting. I reviewed and tested the implementation and aim to explain the commands, configuration and workflow independently.
