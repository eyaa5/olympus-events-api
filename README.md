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

**Base URL (eu-central-1)**  
`https://cspklka3i3.execute-api.eu-central-1.amazonaws.com`

---

## Testing

### With curl (any shell)
```bash
# list all events
curl https://cspklka3i3.execute-api.eu-central-1.amazonaws.com/events

# single event
curl https://cspklka3i3.execute-api.eu-central-1.amazonaws.com/event/e3
