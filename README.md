# Olympus Events API

A tiny serverless API on AWS (Lambda + API Gateway + DynamoDB).

## Endpoints
- `GET /events` – list events
- `GET /event/{id}` – get one event

## Deploy
- Lambda handler: `src/handler.py:lambda_handler`
- Env vars: `TABLE_NAME=olympus_events`

## Testing
Use the Postman collection in `postman/olympus-events.postman_collection.json`.
Set `baseUrl` to your API Gateway base URL.
