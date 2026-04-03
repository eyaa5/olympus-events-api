# AWS Serverless Events API – Production-Ready Backend (Lambda, API Gateway, DynamoDB)

![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-orange)
![API Gateway](https://img.shields.io/badge/AWS-API%20Gateway-yellow)
![DynamoDB](https://img.shields.io/badge/AWS-DynamoDB-blue)
![Made with Python](https://img.shields.io/badge/Python-3.11-informational)
![License: MIT](https://img.shields.io/badge/License-MIT-green)

🚀 Serverless AWS backend project demonstrating real-world cloud architecture and troubleshooting skills.

A production-style serverless REST API built on AWS using API Gateway, Lambda, and DynamoDB.  
This project demonstrates scalable backend architecture and cloud-based API development.

---

## 🧠 System Architecture

Client → API Gateway → AWS Lambda → DynamoDB

- API Gateway receives HTTP requests  
- Lambda processes the logic  
- DynamoDB stores event data  

---

## 🛠️ Troubleshooting & Debugging

### Issue: API Gateway not triggering Lambda
- Cause: Missing integration configuration  
- Fix: Re-linked API Gateway to Lambda  

### Issue: CORS errors
- Cause: Missing CORS headers  
- Fix: Enabled CORS in API Gateway  

### Issue: DynamoDB not returning data
- Cause: Wrong table name or region  
- Fix: Corrected configuration  

### Issue: Permission error
- Cause: IAM role missing permissions  
- Fix: Added DynamoDB permissions  

---

## 💡 What I Learned

- How to build serverless APIs with AWS  
- How API Gateway connects to Lambda  
- How DynamoDB works as a database  
- How to debug cloud applications  
- Importance of IAM roles  

---

## 🚀 Future Improvements

- Add authentication (Cognito)  
- Add logging with CloudWatch  
- Improve error handling  
- Add filtering and pagination  
- Use Infrastructure as Code (Terraform or SAM)  

---

## 🏗️ Architecture Details

- **DynamoDB**: table `olympus_events` (PK: `id`)  
- **Lambda**: `olympus-read-events`  
- **API Gateway (HTTP API)**:  
  - `GET /events` → Lambda  
  - `GET /event/{id}` → Lambda  

> Demo CORS is `*` for simplicity. In production, restrict to your allowed origin(s).

---

## 🔗 Endpoints

- `GET /events` — list all events (supports `?limit=`)  
- `GET /event/{id}` — get a single event (e.g., `e3`)  
- `GET /health` — health check (`{ "ok": true }`)  

---

## 🌍 Live API

Base URL:  
https://cspklka3i3.execute-api.eu-central-1.amazonaws.com

Available endpoints:
- `GET /events`  
- `GET /event/{id}`  
- `GET /health`  

---

## ⚡ Quick curl test

```bash
# list events
curl https://cspklka3i3.execute-api.eu-central-1.amazonaws.com/events

# single event
curl https://cspklka3i3.execute-api.eu-central-1.amazonaws.com/event/e3

# health
curl https://cspklka3i3.execute-api.eu-central-1.amazonaws.com/health
