# Olympus Events API (Serverless on AWS)

![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-orange)
![API Gateway](https://img.shields.io/badge/AWS-API%20Gateway-yellow)
![DynamoDB](https://img.shields.io/badge/AWS-DynamoDB-blue)
![Made with Python](https://img.shields.io/badge/Python-3.11-informational)
![License: MIT](https://img.shields.io/badge/License-MIT-green)

A tiny, production-style **serverless API** that reads events from **DynamoDB** via **AWS Lambda** behind **API Gateway (HTTP API)**.  
Includes a Postman collection and a live base URL.

---

## Architecture

- **DynamoDB**: table `olympus_events` (PK: `id`)
- **Lambda**: `olympus-read-events`
- **API Gateway (HTTP API)**:  
  - `GET /events` → Lambda  
  - `GET /event/{id}` → Lambda

> Demo CORS is `*` for simplicity. In production, restrict to your allowed origin(s).

---

## Endpoints

- `GET /events` — list all events (supports `?limit=`)
- `GET /event/{id}` — get a single event (e.g., `e3`)
- `GET /health` — health check (`{ "ok": true }`)

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
