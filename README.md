# Simple Airflow DAG Project

This project contains a simple Apache Airflow DAG with multiple tasks.

## Setup

1. Install Docker and Docker Compose
2. Clone this repository
3. Run `docker-compose up -d` to start Airflow
4. Access the Airflow web interface at `http://localhost:8080`

## DAG Description

The `multi_task_dag` contains three tasks:

1. A TimeDeltaSensor that waits for 5 minutes
2. A BashOperator that prints the execution date
3. A PythonOperator that prints the execution date with one hour added

The DAG is scheduled to run every 30 minutes.

## Project Structure

- `dags/`: Contains the DAG Python files
- `logs/`: Airflow logs
- `plugins/`: Custom Airflow plugins (if any)
- `Dockerfile`: Defines the Docker image for Airflow
- `docker-compose.yml`: Defines the Airflow services
- `requirements.txt`: Python package dependencies
- `.env`: Environment variables
- `.gitignore`: Specifies files to ignore in Git