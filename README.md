# Olympus Events API (Serverless on AWS)
[![CI](https://github.com/eyaa5/olympus-events-api/actions/workflows/ci.yml/badge.svg)](https://github.com/eyaa5/olympus-events-api/actions/workflows/ci.yml)


![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-orange)
![API Gateway](https://img.shields.io/badge/AWS-API%20Gateway-yellow)
![DynamoDB](https://img.shields.io/badge/AWS-DynamoDB-blue)
![Made with Python](https://img.shields.io/badge/Python-3.11-informational)
![License: MIT](https://img.shields.io/badge/License-MIT-green)
![CI](https://github.com/eyaa5/olympus-events-api/actions/workflows/ci.yml/badge.svg)

A tiny, production-style serverless API that reads events from **DynamoDB** via **AWS Lambda** behind **API Gateway (HTTP API)**.  
Includes IaC (AWS SAM), least-privilege IAM, CI, tests, and a Postman collection.

---

## Endpoints

- `GET /events` — list all events (optional `?limit=` + pagination)
- `GET /event/{id}` — get a single event (e.g., `e3`)
- `GET /health` — quick health check (200 + `{ ok: true }`)
- `GET /` — friendly index with hints

**Live Base URL (eu-central-1)**  
`https://cspklka3i3.execute-api.eu-central-1.amazonaws.com`

### Quick curl test
```bash
# list events
curl https://cspklka3i3.execute-api.eu-central-1.amazonaws.com/events

# single event
curl https://cspklka3i3.execute-api.eu-central-1.amazonaws.com/event/e3

# health
curl https://cspklka3i3.execute-api.eu-central-1.amazonaws.com/health
