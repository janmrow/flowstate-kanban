FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements.txt -r requirements-dev.txt

COPY kanban_app ./kanban_app
COPY tests ./tests

EXPOSE 8000

CMD ["uvicorn", "kanban_app.main:app", "--host", "0.0.0.0", "--port", "8000"]
