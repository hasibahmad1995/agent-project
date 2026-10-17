# Git Tracking Log

Local record of what has been committed and pushed, with descriptions.

Remote: https://github.com/hasibahmad1995/agent-project (public)

## History

1. **Empty repository**: empty root commit (the earlier history was wiped by a force-push).
2. **Add Google Search agent project**: re-added the project files.

| File | Description |
|---|---|
| `app.py` | CLI agent: Groq chat model plus Serper Google Search tool, interactive query loop |
| `requirements.txt` | Python dependencies (`python-dotenv` rather than `dotenv`) |
| `README.md` | Project overview, setup and run instructions |
| `.env.example` | Template listing the required environment variables, with placeholder values |
| `.gitignore` | Excludes `.env`, `.venv/` and Python cache files |
| `GIT_LOG.md` | This tracking file |

Deliberately not committed: `.env` (real API keys) and `.venv/`.
