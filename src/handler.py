import os
import json
from decimal import Decimal

import boto3

# --- Config ---
TABLE_NAME = os.environ.get("TABLE_NAME", "olympus_events")
REGION = os.environ.get("AWS_REGION", "eu-central-1")

ddb = boto3.resource("dynamodb", region_name=REGION)
table = ddb.Table(TABLE_NAME)

CORS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "GET,OPTIONS",
}


# --- helpers ---
def _json_default(o):
    if isinstance(o, Decimal):
        # render DynamoDB Decimals nicely
        return int(o) if o % 1 == 0 else float(o)
    return str(o)


def _resp(status, body, *, is_html=False, extra_headers=None):
    headers = {"Content-Type": "text/html; charset=utf-8" if is_html else "application/json", **CORS}
    if extra_headers:
        headers.update(extra_headers or {})
    return {
        "statusCode": status,
        "headers": headers,
        "body": body if is_html else json.dumps(body, default=_json_default),
    }


# --- routes ---
def lambda_handler(event, context):
    # method + path (covers both HTTP API and REST API shapes)
    method = (event.get("requestContext") or {}).get("http", {}).get("method") or event.get("httpMethod", "GET")
    raw_path = event.get("rawPath") or event.get("path") or "/"
    path = raw_path.rstrip("/") or "/"

    # CORS preflight
    if method == "OPTIONS":
        return _resp(204, "")

    if path == "/":
        return index()

    if path == "/health":
        return _resp(200, {"ok": True})

    if path == "/events":
        return list_events(event)

    if path.startswith("/event/"):
        event_id = path.split("/event/", 1)[1]
        return get_event(event_id)

    return _resp(404, {"ok": False, "message": "Not Found"})


def list_events(event):
    params = event.get("queryStringParameters") or {}
    limit = int(params.get("limit", "100"))

    scan_kwargs = {"Limit": limit}

    # pagination: /events?nextToken=<json>
    if "nextToken" in (params or {}):
        try:
            scan_kwargs["ExclusiveStartKey"] = json.loads(params["nextToken"], parse_float=Decimal)
        except Exception:
            pass

    resp = table.scan(**scan_kwargs)
    items = resp.get("Items", [])

    out = {
        "ok": True,
        "count": len(items),
        "items": items,
    }
    if "LastEvaluatedKey" in resp:
        out["nextToken"] = json.dumps(resp["LastEvaluatedKey"], default=_json_default)

    return _resp(200, out)


def get_event(event_id: str):
    r = table.get_item(Key={"id": event_id})
    item = r.get("Item")
    if not item:
        return _resp(404, {"ok": False, "message": f"Event '{event_id}' not found"})
    return _resp(200, {"ok": True, "item": item})


def index():
    html = """<!doctype html>
<html><head><meta charset="utf-8"><title>Olympus Events API</title></head>
<body style="font-family:system-ui; max-width: 720px; margin: 40px auto;">
  <h2>Olympus Events API</h2>
  <p>Try these endpoints:</p>
  <ul>
    <li><a href="/events">GET /events</a></li>
    <li><a href="/event/e3">GET /event/e3</a> (example)</li>
    <li><a href="/health">GET /health</a></li>
  </ul>
</body></html>"""
    return _resp(200, html, is_html=True)
