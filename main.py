from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "AI Forex Engine Running"}

@app.get("/signal")
def signal():
    return {
        "pair": "EURUSD",
        "signal": "NO TRADE",
        "reason": "Waiting for market structure"
    }
