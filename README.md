# Olympus Events API (Serverless on AWS)

![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-orange)
![API Gateway](https://img.shields.io/badge/AWS-API%20Gateway-yellow)
![DynamoDB](https://img.shields.io/badge/AWS-DynamoDB-blue)
![Made with Python](https://img.shields.io/badge/Python-3.x-informational)
![License: MIT](https://img.shields.io/badge/License-MIT-green)

A tiny, production-style serverless API that reads events from **DynamoDB** via **AWS Lambda** behind **API Gateway (HTTP API)**.  
Live-tested with **Postman** and **curl**.

---

## What’s included
- **Lambda** handler in `src/handler.py` (Python 3.x, JSON, CORS).
- **DynamoDB** table: `olympus_events` (PK: `id`).
- **API Gateway (HTTP API)** routes:
  - `GET /events` — list events (supports `?limit=...`)
  - `GET /event/{id}` — get one event (e.g. `e3`)
- **Postman** collection in `postman/olympus-events.postman_collection.json`.
- Minimal **IAM** least-privilege policy snippet (below).

---

## Base URL (eu-central-1)

