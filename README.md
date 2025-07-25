# Orchestrator

This repository provides a minimal setup to run Apache Airflow using Docker Compose.

## Usage

1. Make sure you have Docker and Docker Compose installed.
2. Clone this repository and navigate to its root directory.
3. Run `docker compose up` to start Airflow.
4. Access the Airflow web interface at [http://localhost:8080](http://localhost:8080) with username `admin` and password `admin`.

The provided `docker-compose.yml` file starts all necessary services, including Postgres, Redis, the Airflow webserver, scheduler, worker, triggerer, and Flower.
