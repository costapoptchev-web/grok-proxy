from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

ZAPIER_WEBHOOK_URL = os.getenv("ZAPIER_WEBHOOK_URL")

@app.post("/grok-sync")
async def grok_sync(request: Request):
    data = await request.json()
    try:
        zap = requests.post(ZAPIER_WEBHOOK_URL, json=data)
        return {
            "status": "✅ Sent to Zapier",
            "zapier_status": zap.status_code,
            "zapier_response": zap.text
        }
    except Exception as e:
        return {"status": "❌ Failed", "error": str(e)}
