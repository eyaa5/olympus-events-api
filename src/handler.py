import os, json, boto3
from decimal import Decimal

TABLE_NAME = os.environ.get("TABLE_NAME", "olympus_events")
REGION = os.environ.get("AWS_REGION", "eu-central-1")
ddb = boto3.resource("dynamodb", region_name=REGION)
table = ddb.Table(TABLE_NAME)

CORS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET,OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
}

def _json_default(o):
    if isinstance(o, Decimal):
        return int(o) if o % 1 == 0 else float(o)
    return str(o)

def _resp(code, body):
    return {"statusCode": code, "headers": {**CORS, "Content-Type": "application/json"},
            "body": json.dumps(body, default=_json_default)}

def lambda_handler(event, context):
    path = (event.get("rawPath") or event.get("path") or "/").strip()
    if path == "/events":
        return list_events(event)
    if path.startswith("/event/"):
        return get_event(path.split("/event/", 1)[1])
    return _resp(404, {"ok": False, "message": "Not Found"})

def list_events(event):
    params = event.get("queryStringParameters") or {}
    limit = int(params.get("limit", "100"))
    resp = table.scan(Limit=limit)
    items = resp.get("Items", [])
    out = {"ok": True, "count": len(items), "items": items}
    lek = resp.get("LastEvaluatedKey")
    if lek: out["nextToken"] = json.dumps(lek, default=_json_default)
    return _resp(200, out)

def get_event(event_id):
    r = table.get_item(Key={"id": event_id})
    item = r.get("Item")
    if not item:
        return _resp(404, {"ok": False, "message": f"Event '{event_id}' not found"})
    return _resp(200, {"ok": True, "item": item})
