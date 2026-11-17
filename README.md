# Student Management API – DevOps Assessment

## Project Overview

A containerized Student Management REST API developed as part of a DevOps Trainee Technical Assessment.

The project uses Flask, PostgreSQL, Nginx, Docker Compose and GitHub Actions.

## Technology Stack

- Ubuntu 24.04 (WSL2)
- Python 3.12
- Flask
- PostgreSQL 16
- Nginx
- Docker and Docker Compose
- Git and GitHub
- pytest
- GitHub Actions

## Architecture

Client → Nginx → Flask API → PostgreSQL

Services:
- Nginx: Reverse proxy, exposed on port 8080.
- Flask: Student Management API, internal port 5000.
- PostgreSQL: Database, internal port 5432.
- Docker Volume: Persistent database storage.

The database port is not published to the host.

## Project Structure

- app/: Flask application and Dockerfile
- nginx/: Nginx reverse proxy configuration
- scripts/: Bash health-check script
- tests/: Automated Python tests
- docs/: Evidence and troubleshooting journal
- .github/workflows/: GitHub Actions CI pipeline
- docker-compose.yml: Multi-container configuration
- .env.example: Environment configuration template

## Setup

Create the environment file:

    cp .env.example .env

Edit `.env` and set a strong database password. Never commit `.env` to Git.

Build and start services:

    docker compose build
    docker compose up -d

Check services:

    docker compose ps

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | API status |
| GET | /health | Application and database health |
| POST | /students | Add a student |
| GET | /students | List students |

Example health check:

    curl http://localhost:8080/health

Example student creation:

    curl -X POST http://localhost:8080/students \
    -H "Content-Type: application/json" \
    -d '{"name":"Aman Gautam"}'

## Automated Testing

Run tests locally:

    python -m pytest -v

The tests cover the home endpoint, student-name validation and health endpoint.

The health endpoint unit test uses a mocked database connection. Actual database connectivity was separately verified through Docker Compose.

## GitHub Actions

Workflow: `.github/workflows/ci.yml`

The pipeline:
1. Checks out the repository.
2. Sets up Python 3.12.
3. Installs dependencies.
4. Validates Python syntax.
5. Runs pytest.
6. Builds the Docker image.

An intentional test failure was demonstrated on a feature branch. The failure was detected by GitHub Actions, corrected, and the pull request was successfully merged.

## Health Check Script

Run:

    ./scripts/health-check.sh

Custom URL:

    ./scripts/health-check.sh http://localhost:8080/health

The script reports the health-check time and result, returning exit code 0 on success and non-zero on failure.

## Security

- Flask application runs as a non-root container user.
- PostgreSQL port is not exposed to the host.
- Database credentials are stored in `.env`.
- `.env` is excluded from Git.
- Nginx configuration is mounted read-only.

## Database Backup and Restore

Create a logical backup:

    docker compose exec -T db sh -c 'pg_dump -U "$POSTGRES_USER" "$POSTGRES_DB"' > backup.sql

Restore:

    cat backup.sql | docker compose exec -T db sh -c 'psql -U "$POSTGRES_USER" "$POSTGRES_DB"'

Backup and restore should be tested before production use. Do not commit backups containing real data.

## Troubleshooting

See `docs/TROUBLESHOOTING.md` for recorded issues, evidence, root causes and resolutions.

## Limitations

- Basic student creation and listing only.
- Authentication is not implemented.
- Health endpoint unit testing uses a mocked database.
- Production HTTPS, monitoring and database migrations require further work.

## AI Assistance Disclosure

AI assistance was used for learning, troubleshooting and drafting parts of the project configuration and documentation. Commands and behavior were tested locally where stated. The author is responsible for understanding and explaining the implementation.
