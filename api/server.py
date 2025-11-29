from fastapi import FastAPI
from pydantic import BaseModel
from simulations.experiments.exp_basic import run as run_basic

app = FastAPI(title="Quantum Ethics Simulator API")


class RunRequest(BaseModel):
    steps: int = 10

@app.post('/run')
def run_sim(req: RunRequest):
    history = run_basic(steps=req.steps)
    return {"status": "ok", "steps": req.steps, "history_length": len(history)}
