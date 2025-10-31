# ai-chatbot

Lightweight AI chatbot (FastAPI backend + Streamlit frontend) demonstrating a Groq/OpenAI-compatible client for model inference. The repo contains a small FastAPI server (`server.py`) exposing a chat API and a Streamlit UI (`frontend.py`) for manual testing.

## Contents

- `server.py` — FastAPI app exposing `/chat` and a conversation clear endpoint.
- `frontend.py` — Streamlit UI that sends messages to the backend.
- `settings.py` — Pydantic settings loader (reads `.env`).
- `model.py` — Pydantic models used by the API.
- `.env` — Local environment variables (gitignored).
- `requirements.txt` — pinned dependencies for the project (generated).

## Features

- Simple REST API for chat interactions
- In-memory conversation history (per-process)
- Streamlit frontend for quick manual testing

## Requirements

- Python 3.10+
- pip
- Recommended Python packages: `fastapi`, `uvicorn`, `streamlit`, `pydantic`, `pydantic-settings`, `requests`, `openai` (or the Groq client compatible package)

Install dependencies (recommended):

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If you prefer to install individual packages, a minimal set is shown below — but `requirements.txt` is provided in this repo so prefer the `-r` flow for reproducibility:

```powershell
python -m pip install fastapi uvicorn streamlit pydantic pydantic-settings requests openai
```

## Configuration

The project reads configuration from a `.env` file via `pydantic-settings`. Create a `.env` in the project root (this repo already includes an example file).

Important variables:

- `GROQ_ENDPOINT` — Groq/OpenAI-compatible base URL
- `GROQ_KEY` — API key/token (keep secret)
- `GROQ_DEPLOYMENT` — Model/deployment name
- `API_URL` — Base URL for the frontend to call (e.g., `http://127.0.0.1:8000`)

Do NOT commit secrets. The included `.gitignore` excludes `.env`.

## Run locally

1. Start the backend (FastAPI):

```powershell
# from project root
uvicorn server:app --host 0.0.0.0 --port 8000 --reload
```

2. Start the Streamlit frontend in a separate shell:

```powershell
streamlit run frontend.py
```

Open the Streamlit UI it serves (usually `http://localhost:8501`) and interact with the chat.

## API

All endpoints are relative to the `API_URL` (default `http://127.0.0.1:8000`).

- POST /chat

  - Request JSON: `{ "message": "Hello" }`
  - Response JSON: `{ "Answer": "Model response text" }` on success, or `{ "Error": "message" }` on error.

- DELETE /clear-conv
  - Clears the in-memory conversation history on the server.

Notes:

- Conversation history is kept in `conversation_hist` (in-memory). Restarting the server clears all history.

## Example

Using curl to send a message:

```powershell
curl -X POST http://127.0.0.1:8000/chat -H "Content-Type: application/json" -d '{"message":"Hello"}'
```

Expected response:

```json
{ "Answer": "Model response text" }
```

## Known issues & suggested fixes

No active issues are known at the moment. The frontend currently calls `/clear-conv` and the backend exposes the same route, and `requirements.txt` is present for reproducible installs.

If you notice anything else (behavioral mismatch, errors, or feature requests), tell me which file you'd like me to change and I can apply a small patch and run a quick smoke test.

## Security and secrets

- Keep your `GROQ_KEY` and other secrets out of source control. Use `.env` (gitignored) or your environment/secret manager in production.

## Docker (optional)

You can containerize the app. A minimal Dockerfile is not included here; if you want one, I can add it.

## Contributing

PRs welcome. For code changes that alter behavior, include tests and update the README accordingly.

## License

MIT

---
