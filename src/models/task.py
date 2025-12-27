"""Task model for the Todo CLI application."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """Represents a single todo task.

    Attributes:
        id: Unique identifier for the task (auto-incremented)
        user_id: User identifier who owns this task
        title: Brief description of the task (required)
        description: Detailed information about the task (optional)
        completed: Whether the task has been completed (default False)
    """

    id: int
    user_id: int
    title: str
    description: str = ""
    completed: bool = False
