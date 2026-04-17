# TechX Sentiment Analysis

TechX is a small sentiment analysis project with:

- a FastAPI backend
- a browser-based frontend served by the API
- two sentiment implementations for comparison:
  `Hugging Face Transformers` for the live API and `TextBlob` for baseline evaluation
- evaluation scripts and basic backend tests

The API classifies text as `Positive`, `Negative`, or `Neutral`.

## Current Behavior

- `GET /` serves the frontend from `Frontend/frontend.html`
- `GET /health` returns a simple health check
- `POST /analyze` uses the Hugging Face model in [Backend/app/sentiment_hf.py](/c:/Users/jackd/OneDrive/Documents/Projects/Techx/Backend/app/sentiment_hf.py)
- the response currently returns:
  `text`, `sentiment`, `score`, `model`, `polarity`, and `subjectivity`
- `polarity` and `subjectivity` are currently `null` in the API response because the live endpoint is not using the TextBlob analyzer

## Project Structure

```text
Techx/
|-- Backend/
|   |-- app/
|   |   |-- __init__.py
|   |   |-- main.py
|   |   |-- sentiment.py
|   |   `-- sentiment_hf.py
|   |-- tests/
|   |   |-- conftest.py
|   |   |-- test_api.py
|   |   `-- test_sentiment.py
|   |-- evaluation_samples.json
|   |-- requirements.txt
|   |-- run_evaluation_hf.py
|   |-- run_evaluation_textblob.py
|   `-- sentiment_evaluation.ipynb
|-- Frontend/
|   `-- frontend.html
|-- README.md
`-- REPORT.md
```

## Setup

From the repo root:

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r Backend\requirements.txt
python -m pip install transformers torch
```

`transformers` and `torch` are needed for the Hugging Face model used by the live API.

## Run the API

From the repo root:

```bash
uvicorn Backend.app.main:app --reload
```

Open:

- App: `http://127.0.0.1:8000/`
- Docs: `http://127.0.0.1:8000/docs`
- Health: `http://127.0.0.1:8000/health`

## Example Request

```bash
curl -X POST "http://127.0.0.1:8000/analyze" ^
  -H "Content-Type: application/json" ^
  -d "{\"text\":\"The product works really well and I enjoy using it.\"}"
```

## Example Response

```json
{
  "text": "The product works really well and I enjoy using it.",
  "sentiment": "Positive",
  "score": 0.9876,
  "model": "cardiffnlp/twitter-roberta-base-sentiment-latest",
  "polarity": null,
  "subjectivity": null
}
```

## Evaluation Scripts

Run these from the `Backend` directory:

```bash
cd Backend
python run_evaluation_hf.py
python run_evaluation_textblob.py
```

- `run_evaluation_hf.py` evaluates the Hugging Face model used by the API
- `run_evaluation_textblob.py` evaluates the TextBlob baseline analyzer
- both scripts use `evaluation_samples.json`

## Tests

From the `Backend` directory:

```bash
pytest
```

## Sentiment Implementations

### Hugging Face

The live API uses `cardiffnlp/twitter-roberta-base-sentiment-latest` through the `transformers` pipeline in [Backend/app/sentiment_hf.py](/c:/Users/jackd/OneDrive/Documents/Projects/Techx/Backend/app/sentiment_hf.py).

### TextBlob

The baseline analyzer in [Backend/app/sentiment.py](/c:/Users/jackd/OneDrive/Documents/Projects/Techx/Backend/app/sentiment.py) uses polarity thresholds:

- polarity `> 0.2` -> `Positive`
- polarity `< -0.2` -> `Negative`
- otherwise -> `Neutral`

## Sample Evaluation Set

The evaluation file contains 12 labeled examples:

- 4 positive
- 4 negative
- 4 neutral

These are useful for quick regression checks while comparing the Hugging Face and TextBlob approaches.
