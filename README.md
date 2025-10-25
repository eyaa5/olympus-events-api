# Olympus Events API (Serverless on AWS)

![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-orange)
![API Gateway](https://img.shields.io/badge/AWS-API%20Gateway-yellow)
![DynamoDB](https://img.shields.io/badge/AWS-DynamoDB-blue)
![Made with Python](https://img.shields.io/badge/Python-3.x-informational)
![License: MIT](https://img.shields.io/badge/License-MIT-green)

A tiny, production-style serverless API that reads events from **DynamoDB** via **AWS Lambda** behind **API Gateway (HTTP API)**.  
Live-tested with **Postman**.

---

## Endpoints

- `GET /events` — list all events
- `GET /event/{id}` — get a single event (e.g. `e3`)

**Base URL (eu-central-1):**  
`https://cspklka3i3.execute-api.eu-central-1.amazonaws.com`

---

## Quick start

```bash
# 1) clone
git clone https://github.com/eyaa5/olympus-events-api.git
cd olympus-events-api

# 2) test the live API
curl https://cspklka3i3.execute-api.eu-central-1.amazonaws.com/events
curl https://cspklka3i3.execute-api.eu-central-1.amazonaws.com/event/e3
