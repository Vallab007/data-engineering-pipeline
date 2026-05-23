# End-to-End Data Engineering Pipeline

## Authors
- Sreejha Kurapati
- Sreepada Vallab Kandi

---

# Project Overview

This project demonstrates a Dockerized end-to-end data engineering pipeline built using Apache Kafka, Apache Spark, Apache Airflow, PostgreSQL, and Docker Compose.

The pipeline automates data ingestion, streaming, processing, orchestration, and storage for scalable ETL workflows.

---

# Tools & Technologies Used

- Apache Kafka
- Apache Spark
- Apache Airflow
- PostgreSQL
- Docker & Docker Compose
- Python

---

# Architecture Overview

1. Data is streamed from an API into Kafka topics.
2. Apache Spark consumes and processes streaming data.
3. Airflow orchestrates ETL workflows and scheduling.
4. Processed data is stored inside PostgreSQL.
5. Docker Compose manages all services and containers.

---

# Objective

The goal of this project is to understand real-world data engineering workflows including:

- Streaming pipelines
- Workflow orchestration
- Distributed data processing
- Containerized deployment
- Real-time event processing

---

# Original Reference

This project was customized and enhanced based on an open-source implementation for learning and portfolio purposes.

---

# Detailed Workflow

## 1. Data Streaming

Initially, data is streamed from the API into a Kafka topic.

## 2. Data Processing

A Spark job consumes the streaming data from Kafka and transfers the processed data into a PostgreSQL database.

## 3. Scheduling with Airflow

Both the streaming task and Spark jobs are orchestrated using Apache Airflow.

In a production environment, Kafka producers continuously listen to APIs or event streams. For demonstration purposes, this project schedules streaming tasks periodically using Airflow DAGs.

---

# Team Collaboration

This project demonstrates collaborative development using GitHub workflows and version control practices.

## Features

- Real-time event streaming with Kafka
- Dockerized multi-container architecture
- Kafka producer and consumer implementation
- Event-driven data pipeline simulation
- Collaborative GitHub workflow
- Scalable ETL architecture

---

# Team Members

- Sreejha Kurapati
- Sreepada Vallab Kandi

---

# Dockerized Deployment

All services in this project are containerized and managed using Docker Compose.

Services include:

- Kafka
- Zookeeper
- Spark
- Airflow
- PostgreSQL
- Producer & Consumer applications

---

# Future Enhancements

- Integrate real-time dashboards
- Add cloud deployment (AWS/GCP/Azure)
- Implement monitoring and logging
- Add CI/CD pipeline integration
- Extend Spark streaming transformations

---

# Architecture Diagram

![Architecture Diagram](https://github.com/HamzaG737/data-engineering-project/assets/71135893/ce92b731-038a-4d9c-9722-f97a6ba51153)
