from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from textblob import TextBlob


POSITIVE_THRESHOLD = 0.2
NEGATIVE_THRESHOLD = -0.2


@dataclass
class SentimentResult:
    label: str
    polarity: float
    subjectivity: float


def validate_text_input(text: Any) -> str:
    # Ensure the input is a non-empty string.
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")

    cleaned = text.strip()
    if not cleaned:
        raise ValueError("Input cannot be empty.")

    return cleaned


def analyze_sentiment(text: Any) -> SentimentResult:
    # Run sentiment analysis using TextBlob polarity.
    cleaned = validate_text_input(text)
    blob = TextBlob(cleaned)
    polarity = float(blob.sentiment.polarity)
    subjectivity = float(blob.sentiment.subjectivity)

    if polarity > POSITIVE_THRESHOLD:
        label = "Positive"
    elif polarity < NEGATIVE_THRESHOLD:
        label = "Negative"
    else:
        label = "Neutral"

    return SentimentResult(
        label=label,
        polarity=round(polarity, 4),
        subjectivity=round(subjectivity, 4),
    )
