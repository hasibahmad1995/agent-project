# Agent Project

A small command-line agent that answers questions using Google Search. It uses LangChain's `create_agent` with a Groq-hosted model and the Serper Google Search API as its only tool.

## Setup

1. Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and fill in your keys:
   - `GROQ_API_KEY` from https://console.groq.com
   - `SERPER_API_KEY` from https://serper.dev

## Run

```
python app.py
```

Type a question at the prompt. Type `exit` or `quit` to stop. It needs an interactive terminal because it reads input with `input()`.

## Notes

- Each question is sent to the agent on its own, so the agent does not remember earlier turns.
- Never commit `.env`. It is listed in `.gitignore`.
