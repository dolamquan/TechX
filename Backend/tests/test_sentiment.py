from __future__ import annotations

import pytest

from app.sentiment import analyze_sentiment, validate_text_input


def test_validate_text_input_rejects_non_string() -> None:
    with pytest.raises(ValueError, match="Input must be a string."):
        validate_text_input(123)


def test_validate_text_input_rejects_empty_text() -> None:
    with pytest.raises(ValueError, match="Input cannot be empty."):
        validate_text_input("   ")


def test_analyze_sentiment_returns_positive_label() -> None:
    result = analyze_sentiment("I love this product.")
    assert result.label == "Positive"


def test_analyze_sentiment_returns_negative_label() -> None:
    result = analyze_sentiment("I hate how broken this app is.")
    assert result.label == "Negative"
