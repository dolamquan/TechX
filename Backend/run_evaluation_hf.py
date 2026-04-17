from __future__ import annotations

import json
from pathlib import Path

from app.sentiment_hf import analyze_sentiment_hf


def main() -> None:
    samples_path = Path("evaluation_samples.json")
    samples = json.loads(samples_path.read_text(encoding="utf-8"))

    correct = 0
    total = len(samples)
    model_name = ""

    print("Hugging Face Sentiment Evaluation Results")
    print("-" * 88)

    for index, sample in enumerate(samples, start=1):
        result = analyze_sentiment_hf(sample["text"])
        predicted = result["label"].capitalize()
        confidence = result["score"]
        expected = sample["expected"]
        is_correct = predicted == expected
        correct += int(is_correct)
        model_name = result["model"]

        print(
            f"{index:>2}. expected={expected:<8} predicted={predicted:<8} "
            f"score={confidence:<6} text={sample['text']}"
        )

    accuracy = correct / total if total else 0.0
    print("-" * 88)
    if model_name:
        print(f"Model: {model_name}")
    print(f"Accuracy: {correct}/{total} = {accuracy:.2%}")


if __name__ == "__main__":
    main()
