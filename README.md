# TechX AI Engineering Basics: Sentiment Analysis Mini Project

This project is a small FastAPI backend that accepts text input and returns a sentiment label:

- `Positive`
- `Negative`
- `Neutral`

It uses `TextBlob` as the NLP library and includes:

- basic validation for empty and non-string input
- a `/analyze` API endpoint
- a `/health` API endpoint
- a browser frontend served from `/`
- a 12-sentence evaluation script
- a short analysis of likely incorrect or uncertain predictions

## Project Structure

```text
.
|-- app/
|   |-- main.py
|   `-- sentiment.py
|-- tests/
|   `-- test_sentiment.py
|-- evaluation_samples.json
|-- requirements.txt
|-- run_evaluation.py
`-- README.md
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Run the API

```bash
uvicorn app.main:app --reload
```

Open the interactive docs at:

```text
http://127.0.0.1:8000/docs
```

Open the frontend at:

```text
http://127.0.0.1:8000/
```

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
  "polarity": 0.85,
  "subjectivity": 0.7
}
```

## Evaluate on 12 Sentences

```bash
python run_evaluation.py
```

## Notes on Incorrect or Uncertain Predictions

1. `"I tried the new version yesterday and it has a different layout."`
   This sentence is intended to be neutral, but a lexicon-based model may treat `"different"` as weakly opinionated depending on context and produce a slightly non-neutral score.

2. `"The update made the dashboard clearer and easier to use."`
   This should be positive, but if the model does not strongly weight `"clearer"` or `"easier"`, the polarity may land close to neutral and become uncertain.

These edge cases show a common limitation of simple sentiment tools: they rely on word-level polarity and do not fully understand product context, tone, or implied meaning.
