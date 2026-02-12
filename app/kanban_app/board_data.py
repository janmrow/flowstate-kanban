from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable


class Status(str, Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"


class Priority(str, Enum):
    P0 = "P0"
    P1 = "P1"
    P2 = "P2"


@dataclass(frozen=True)
class Task:
    id: int
    title: str
    priority: Priority
    status: Status


def get_seed_tasks() -> list[Task]:
    # Simple in-memory seed; later this will come from DB.
    return [
        Task(
            id=1,
            title="Write health endpoint",
            priority=Priority.P2,
            status=Status.DONE,
        ),
        Task(
            id=2,
            title="Render Kanban board UI",
            priority=Priority.P1,
            status=Status.IN_PROGRESS,
        ),
        Task(id=3, title="Add drag & drop", priority=Priority.P0, status=Status.TODO),
        Task(
            id=4,
            title="Add filters and search",
            priority=Priority.P1,
            status=Status.TODO,
        ),
    ]


def by_status(tasks: Iterable[Task], status: Status) -> list[Task]:
    return [t for t in tasks if t.status == status]
