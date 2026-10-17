# Git Tracking Log

Local record of what has been committed and pushed, with descriptions.

Remote: https://github.com/hasibahmad1995/agent-project (public)

## History

The repo was deleted and recreated, so history has a single commit.

1. **Add Google Search agent project** (`a95ac6c`): initial commit with the files below.

| File | Description |
|---|---|
| `app.py` | CLI agent: Groq chat model plus Serper Google Search tool, interactive query loop |
| `requirements.txt` | Python dependencies (`python-dotenv` rather than `dotenv`) |
| `README.md` | Project overview, setup and run instructions |
| `.env.example` | Template listing the required environment variables, with placeholder values |
| `.gitignore` | Excludes `.env`, `.venv/` and Python cache files |
| `GIT_LOG.md` | This tracking file |

Deliberately not committed: `.env` (real API keys) and `.venv/`.
