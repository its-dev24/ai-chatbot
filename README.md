# ai-chatbot

Lightweight AI chatbot (FastAPI backend + Streamlit frontend) that demonstrates using a Groq-compatible client for model inference. This repo provides a small local server (`server.py`) that exposes a chat API and a simple Streamlit-based frontend (`frontend.py`).

## Contents

- `server.py` — FastAPI app exposing `/chat` and a conversation clear endpoint.
- `frontend.py` — Streamlit UI that sends messages to the backend.
- `settings.py` — Pydantic settings loader (reads `.env`).
- `model.py` — Pydantic models used by the API.
- `.env` — Local environment variables (gitignored).

## Features

- Simple REST API for chat interactions
- In-memory conversation history (per-process)
- Streamlit frontend for quick manual testing

## Requirements

- Python 3.10+
- pip
- Recommended Python packages: `fastapi`, `uvicorn`, `streamlit`, `pydantic`, `pydantic-settings`, `requests`, `openai` (or the Groq client compatible package)

If you don't have a `requirements.txt`, a minimal install is:

```powershell
python -m pip install --upgrade pip
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

- Endpoint name mismatch: `frontend.py` calls the clear route at `/clear-convo` but the backend defines `/clear-conv`. To fix, either:

  - Update `frontend.py` to call `/clear-conv` (quick fix), or
  - Change the backend route to match the frontend.

  Suggested frontend change (in `frontend.py`):

  - Replace `/clear-convo` with `/clear-conv`.

- Conversation clearing bug in backend: `clear_convo` currently assigns `conversation_hist = []` inside the function which creates a local variable and doesn't clear the module-level list. Replace the function body with `conversation_hist.clear()` (or declare `global conversation_hist` and reassign) to clear the shared list.

## Security and secrets

- Keep your `GROQ_KEY` and other secrets out of source control. Use `.env` (gitignored) or your environment/secret manager in production.

## Docker (optional)

You can containerize the app. A minimal Dockerfile is not included here; if you want one, I can add it.

## Contributing

PRs welcome. For code changes that alter behavior, include tests and update the README accordingly.

## License

MIT

---

If you'd like, I can also:

- Patch the endpoint name mismatch in `frontend.py` or `server.py`.
- Fix the `clear_convo` bug so the DELETE action actually clears the server conversation history.
- Add a `requirements.txt` listing the exact packages used.

Tell me which of the above (if any) you'd like me to do next.
