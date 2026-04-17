from __future__ import annotations

from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette.responses import FileResponse

from .sentiment_hf import analyze_sentiment_hf


app = FastAPI(
    title="TechX Sentiment Analysis API",
    description="Mini FastAPI backend for classifying text as Positive, Negative, or Neutral.",
    version="1.0.0",
)

FRONTEND_PATH = Path(__file__).resolve().parents[2] / "Frontend" / "frontend.html"


class SentimentRequest(BaseModel):
    text: Any


@app.get("/", include_in_schema=False)
def serve_frontend() -> FileResponse:
    if not FRONTEND_PATH.exists():
        raise HTTPException(status_code=404, detail="Frontend file not found.")
    return FileResponse(FRONTEND_PATH)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/analyze")
def analyze(request: SentimentRequest) -> dict[str, Any]:
    try:
        result = analyze_sentiment_hf(request.text)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return {
        "text": request.text,
        "sentiment": result["label"],
        "polarity": result["polarity"],
        "subjectivity": result["subjectivity"],
    }
