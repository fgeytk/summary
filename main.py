from fastapi import FastAPI
from model import SummarizationRequest
from summarizer import generate_summary

app = FastAPI()

@app.post("/summarize")
def summarize(req: SummarizationRequest):
    result = generate_summary(req.text, req.mode)
    return {
        "original_text": req.text,
        "mode": req.mode,
        "summary": result
    }