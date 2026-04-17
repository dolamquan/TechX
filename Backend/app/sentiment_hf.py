from __future__ import annotations

from typing import Any

from transformers import pipeline


MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment-latest"
LABEL_MAP = {
    "LABEL_0": "Negative",
    "LABEL_1": "Neutral",
    "LABEL_2": "Positive",
}

_classifier = pipeline("text-classification", model=MODEL_NAME)


def analyze_sentiment_hf(text: Any) -> dict[str, Any]:
    # Validate input to match the API's backend expectations.
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")

    cleaned = text.strip()
    if not cleaned:
        raise ValueError("Input cannot be empty.")

    result = _classifier(cleaned)[0]
    label = LABEL_MAP.get(result["label"], result["label"])

    return {
        "label": label,
        "score": round(float(result["score"]), 4),
        "model": MODEL_NAME,
    }
