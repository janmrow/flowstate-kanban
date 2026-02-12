from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from kanban_app.board_data import Status, by_status, get_seed_tasks

app = FastAPI(title="Kanban", version="0.1.0")

templates = Jinja2Templates(directory="kanban_app/templates")
app.mount("/static", StaticFiles(directory="kanban_app/static"), name="static")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def board(request: Request) -> HTMLResponse:
    tasks = get_seed_tasks()
    context = {
        "request": request,
        "todo": by_status(tasks, Status.TODO),
        "in_progress": by_status(tasks, Status.IN_PROGRESS),
        "done": by_status(tasks, Status.DONE),
    }
    return templates.TemplateResponse("board.html", context)
