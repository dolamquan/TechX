# Sentiment Analysis Mini Project Report

## Objective

Build a simple sentiment analysis application that accepts text input and classifies it as `Positive`, `Negative`, or `Neutral`.

The current project delivers this through:

- a FastAPI backend
- a browser frontend served by the backend
- a Hugging Face sentiment model for the live `/analyze` API
- a separate TextBlob implementation for baseline comparison

## Implementation Summary

The main API is defined in [Backend/app/main.py](/c:/Users/jackd/OneDrive/Documents/Projects/Techx/Backend/app/main.py). It exposes:

- `GET /` to serve the frontend
- `GET /health` to confirm the API is running
- `POST /analyze` to classify input text

The live `/analyze` endpoint currently uses the Hugging Face pipeline in [Backend/app/sentiment_hf.py](/c:/Users/jackd/OneDrive/Documents/Projects/Techx/Backend/app/sentiment_hf.py), based on the model:

`cardiffnlp/twitter-roberta-base-sentiment-latest`

The project also keeps a TextBlob-based analyzer in [Backend/app/sentiment.py](/c:/Users/jackd/OneDrive/Documents/Projects/Techx/Backend/app/sentiment.py) for comparison and evaluation.

## Library Choices

### Hugging Face Transformers

The live API uses Hugging Face because it provides a stronger pretrained sentiment model than a simple lexicon-based approach. The model returns:

- a predicted label
- a confidence score
- the model name used for inference

This makes the main API more realistic and easier to inspect during testing.

### TextBlob

TextBlob is still useful here as a lightweight baseline. It computes polarity and subjectivity, then maps polarity to labels using these thresholds:

- `Positive` if polarity is greater than `0.2`
- `Negative` if polarity is less than `-0.2`
- `Neutral` otherwise

Keeping both implementations makes it easier to compare a classic rule-based baseline with a modern pretrained model.

## Validation

Both analyzers enforce the same basic input checks:

- reject non-string input
- reject empty or whitespace-only strings

Invalid input returns HTTP `400` from the API with a clear error message.

## API Response

The `/analyze` endpoint currently returns:

- `text`
- `sentiment`
- `score`
- `model`
- `polarity`
- `subjectivity`

Because the live endpoint uses the Hugging Face model, `polarity` and `subjectivity` are currently returned as `null`. Those values are only produced by the separate TextBlob analyzer.

## Evaluation Set

The evaluation dataset in [Backend/evaluation_samples.json](/c:/Users/jackd/OneDrive/Documents/Projects/Techx/Backend/evaluation_samples.json) contains 12 labeled samples:

- 4 positive
- 4 negative
- 4 neutral

This gives a small but balanced set for quick regression checks.

## Evaluation Workflow

The project includes two evaluation scripts:

- [Backend/run_evaluation_hf.py](/c:/Users/jackd/OneDrive/Documents/Projects/Techx/Backend/run_evaluation_hf.py) for the Hugging Face model used by the API
- [Backend/run_evaluation_textblob.py](/c:/Users/jackd/OneDrive/Documents/Projects/Techx/Backend/run_evaluation_textblob.py) for the TextBlob baseline

This split is useful because it lets the project compare the production API path with the simpler baseline implementation.

## Analysis of Two Uncertain Cases

1. `I tried the new version yesterday and it has a different layout.`
   This sentence is intended to be neutral, but it can be tricky because the word `different` may be interpreted as weak sentiment even when the sentence is only descriptive.

2. `The update made the dashboard clearer and easier to use.`
   This sentence is clearly positive to a human reader, but some models may underweight product-usability language if it does not contain strongly emotional words.

These cases show why sentiment analysis is still context-sensitive: even good models can struggle when the tone is subtle, descriptive, or tied to product experience rather than explicit emotion.

## Conclusion

This project now goes beyond the minimum TextBlob-only version by combining:

- a FastAPI service
- a polished frontend
- a pretrained Hugging Face sentiment model for the live API
- a TextBlob baseline for comparison
- a small labeled evaluation set and test suite

Overall, it demonstrates both a practical API implementation and a useful comparison between two sentiment analysis approaches.
