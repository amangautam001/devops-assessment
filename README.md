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
- Nginx: Reverse proxy, bound to 127.0.0.1:8080 (local machine only).
- Flask: Student Management API, internal port 5000.
- PostgreSQL: Database, internal port 5432.
- Docker Volume: Persistent database storage.

The database port is not published to the host.

             Local Client
                  |
                  v
          localhost:8080
                  |
                  v
             Nginx
          (127.0.0.1:8080)
                  |
                  v
             Flask API
              :5000
                  |
                  v
           PostgreSQL
              :5432
                  |
                  v
          postgres_data
          (Docker Volume)

## Project Structure

- app/: Flask application and Dockerfile
- nginx/: Nginx reverse proxy configuration
- scripts/: Bash health-check script
- tests/: Automated Python tests
- docs/: Evidence and troubleshooting journal
- .github/workflows/: GitHub Actions CI pipeline
- docker-compose.yml: Multi-container configuration
- .env.example: Environment configuration template

## Prerequisites

- Windows 11 with WSL2 and Ubuntu 24.04, or an equivalent Ubuntu environment.
- Docker Engine with Docker Compose plugin.
- Git.
- Python 3.12 for running tests locally.
- curl for API validation.

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

PostgreSQL supports logical backups using `pg_dump`.

### Create Backup

    docker compose exec -T db sh -c 'pg_dump -U "$POSTGRES_USER" "$POSTGRES_DB"' > /tmp/studentdb-backup.sql

### Restore to a Test Database

Create a temporary database:

    docker compose exec db sh -c 'createdb -U "$POSTGRES_USER" studentdb_restore_test'

Restore the backup:

    cat /tmp/studentdb-backup.sql | docker compose exec -T db sh -c 'psql -v ON_ERROR_STOP=1 -U "$POSTGRES_USER" studentdb_restore_test'

Verify restored records:

    docker compose exec db sh -c 'psql -U "$POSTGRES_USER" -d studentdb_restore_test -c "SELECT id, name FROM students;"'

Remove the temporary test database after verification:

    docker compose exec db sh -c 'dropdb -U "$POSTGRES_USER" studentdb_restore_test'

### Verification

A local backup and restore test was performed using a temporary database. The restored student record was verified successfully, and the original database remained unchanged.

**Note:** Keep backups secure and never commit database backups containing private or real customer data.
## Troubleshooting

See `docs/TROUBLESHOOTING.md` for recorded issues, evidence, root causes and resolutions.

## Limitations

- Basic student creation and listing only.
- Authentication is not implemented.
- Health endpoint unit testing uses a mocked database.
- Production HTTPS, monitoring and database migrations require further work.

## AI Assistance Disclosure

AI assistance was used for learning, troubleshooting and drafting parts of the project configuration and documentation. Commands and behavior were tested locally where stated. The author is responsible for understanding and explaining the implementation.

## Shutdown

Stop and remove application containers:

    docker compose down

This preserves the PostgreSQL named volume and existing database data.

To start the environment again:

    docker compose up -d

Do not use `docker compose down -v` unless you intentionally want to delete the database volume and its stored data.
