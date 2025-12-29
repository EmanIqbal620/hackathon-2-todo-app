"""Task model for the Todo CLI application."""

from dataclasses import dataclass, field
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
        priority: Task priority level (High/Medium/Low, default Medium)
        category: Task category (Work/Home/Personal, default Personal)
        due_date: Due date for the task (optional, YYYY-MM-DD format)
        updated_flag: Whether the task has been modified
        recurrence_pattern: Recurrence frequency (None/Daily/Weekly/Monthly)
        reminder_offset: When to show reminder (None/1 day/1 hour/At due)
        reminder_shown: Whether reminder has been displayed for this task
    """

    id: int
    user_id: int
    title: str
    description: str = ""
    completed: bool = False
    priority: str = "Medium"
    category: str = "Personal"
    due_date: str = ""
    updated_flag: bool = False
    recurrence_pattern: str = "None"
    reminder_offset: str = "None"
    reminder_shown: bool = False


# Priority and category constants
PRIORITY_LEVELS = ["High", "Medium", "Low"]
CATEGORY_OPTIONS = ["Work", "Home", "Personal"]

# Recurrence and reminder constants
RECURRENCE_PATTERNS = ["None", "Daily", "Weekly", "Monthly"]
REMINDER_OFFSETS = ["None", "1 day", "1 hour", "At due"]
