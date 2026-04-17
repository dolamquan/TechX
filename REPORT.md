# Sentiment Analysis Mini Project Report

## Objective

Build a simple API that accepts text input and predicts sentiment as `Positive`, `Negative`, or `Neutral`.

## Library Choice

This implementation uses `TextBlob`, a lightweight NLP library that provides sentence polarity and subjectivity scores. The polarity score is mapped to:

- `Positive` if polarity is greater than `0.1`
- `Negative` if polarity is less than `-0.1`
- `Neutral` otherwise

## Validation

The API performs two required validation checks:

- Rejects empty input strings
- Rejects non-string input values

Invalid requests return an HTTP `400` response with a clear error message.

## Evaluation Set

The project includes 12 test sentences:

- 4 positive
- 4 negative
- 4 neutral

They are stored in `evaluation_samples.json` and evaluated by `run_evaluation.py`.

## Analysis of Two Incorrect or Uncertain Predictions

1. `I tried the new version yesterday and it has a different layout.`
   This sentence is intended to be neutral, but the model may see `"different"` as mildly positive or negative without understanding that the sentence is mostly descriptive.

2. `The update made the dashboard clearer and easier to use.`
   This sentence is positive, but simple lexicon-based sentiment models can under-score usability improvements because the positive meaning depends on product context rather than strongly emotional words.

## Conclusion

This solution meets the assignment requirements with a clean FastAPI backend, reusable sentiment logic, basic input validation, and a small evaluation workflow.
