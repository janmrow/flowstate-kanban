# Kanban (Python + FastAPI + Playwright)

This repo contains a simple Kanban web application along with an automated testing suite and deployment configuration.

## Tech Stack
- **Backend:** FastAPI
- **Testing:** Playwright (Python)
- **DevOps:** Docker, GitHub Actions

## Run locally (app)

1. Navigate to the app directory:
   ```bash
   cd app
   ```
2. Set up the virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt -r requirements-dev.txt
   ```
3. Start the server:
   ```bash
   uvicorn kanban_app.main:app --reload --port 8000
   ```

## API Status & Documentation

Once the app is running, you can access:
* **Health check:** [http://localhost:8000/health](http://localhost:8000/health)
* **Interactive API Docs (Swagger):** [http://localhost:8000/docs](http://localhost:8000/docs)

## Testing

To run E2E tests with Playwright:
```bash
# Run tests
pytest
```
