from fastapi.testclient import TestClient

from kanban_app.main import app


def test_board_page_renders_basic_structure() -> None:
    client = TestClient(app)
    resp = client.get("/")
    assert resp.status_code == 200
    html = resp.text

    # Basic testids (stable hooks for E2E later)
    assert 'data-testid="board"' in html
    assert 'data-testid="column-TODO"' in html
    assert 'data-testid="column-IN_PROGRESS"' in html
    assert 'data-testid="column-DONE"' in html
