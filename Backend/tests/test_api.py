from __future__ import annotations

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root_serves_frontend() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "TechX Sentiment Analysis" in response.text


def test_analyze_endpoint_returns_sentiment_payload() -> None:
    response = client.post("/analyze", json={"text": "I love this feature."})

    assert response.status_code == 200
    body = response.json()
    assert body["text"] == "I love this feature."
    assert body["sentiment"] in {"Positive", "Negative", "Neutral"}
    assert isinstance(body["polarity"], float)
    assert isinstance(body["subjectivity"], float)
