from __future__ import annotations

import json
from pathlib import Path

from app.sentiment import analyze_sentiment


def main() -> None:
    samples_path = Path("evaluation_samples.json")
    samples = json.loads(samples_path.read_text(encoding="utf-8"))

    correct = 0
    total = len(samples)

    print("Sentiment Evaluation Results")
    print("-" * 72)

    for index, sample in enumerate(samples, start=1):
        result = analyze_sentiment(sample["text"])
        predicted = result.label
        expected = sample["expected"]
        is_correct = predicted == expected
        correct += int(is_correct)

        print(
            f"{index:>2}. expected={expected:<8} predicted={predicted:<8} "
            f"polarity={result.polarity:<6} text={sample['text']}"
        )

    accuracy = correct / total if total else 0.0
    print("-" * 72)
    print(f"Accuracy: {correct}/{total} = {accuracy:.2%}")


if __name__ == "__main__":
    main()
