"""Task service for managing todo tasks in memory."""

import calendar
from datetime import datetime, timedelta
from typing import List, Optional, Tuple
from models.task import Task, RECURRENCE_PATTERNS, REMINDER_OFFSETS


def _validate_date_format(date_str: str) -> bool:
    """Validate date string is in YYYY-MM-DD format and is a valid date.

    Args:
        date_str: The date string to validate

    Returns:
        True if valid YYYY-MM-DD format, False otherwise
    """
    if not date_str:
        return True  # Empty is valid (optional field)
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def _add_months(date: datetime, months: int) -> datetime:
    """Add months to a date, handling month-end edge cases.

    Args:
        date: The base date
        months: Number of months to add

    Returns:
        New datetime with months added
    """
    month = date.month + months
    year = date.year + (month - 1) // 12
    month = ((month - 1) % 12) + 1
    # Handle month-end edge case (e.g., Jan 31 -> Feb 28)
    day = min(date.day, calendar.monthrange(year, month)[1])
    return date.replace(year=year, month=month, day=day)


def _calculate_next_due_date(current_due: str, pattern: str) -> str:
    """Calculate next due date based on recurrence pattern.

    Args:
        current_due: Current due date in YYYY-MM-DD format
        pattern: Recurrence pattern (Daily/Weekly/Monthly)

    Returns:
        Next due date in YYYY-MM-DD format
    """
    if not current_due or pattern == "None":
        return ""

    try:
        due_date = datetime.strptime(current_due, "%Y-%m-%d")

        if pattern == "Daily":
            next_date = due_date + timedelta(days=1)
        elif pattern == "Weekly":
            next_date = due_date + timedelta(days=7)
        elif pattern == "Monthly":
            next_date = _add_months(due_date, 1)
        else:
            return current_due

        return next_date.strftime("%Y-%m-%d")
    except ValueError:
        return current_due


class TaskService:
    """Manages task operations with in-memory storage.

    Attributes:
        tasks: List of Task objects stored in memory
        next_id: Auto-incrementing ID counter for new tasks
    """

    def __init__(self) -> None:
        """Initialize the task service with an empty list and ID counter."""
        self.tasks: List[Task] = []
        self.next_id: int = 1

    def is_overdue(self, task: Task) -> bool:
        """Check if a task is overdue.

        A task is overdue if:
        - It has a due_date
        - It is not completed
        - The due_date is before today's date

        Args:
            task: The Task object to check

        Returns:
            True if the task is overdue, False otherwise
        """
        if not task.due_date or task.completed:
            return False
        try:
            due = datetime.strptime(task.due_date, "%Y-%m-%d").date()
            today = datetime.now().date()
            return due < today
        except ValueError:
            return False

    def add_task(
        self,
        user_id: int,
        title: str,
        description: str = "",
        priority: str = "Medium",
        category: str = "Personal",
        due_date: str = "",
        recurrence_pattern: str = "None",
        reminder_offset: str = "None"
    ) -> Task:
        """Create a new task with auto-incremented ID.

        Args:
            user_id: The user ID who owns this task
            title: Brief description of the task (required)
            description: Detailed information about the task (optional)
            priority: Task priority level (High/Medium/Low, default Medium)
            category: Task category (Work/Home/Personal, default Personal)
            due_date: Due date for the task (optional, YYYY-MM-DD format)
            recurrence_pattern: Recurrence frequency (None/Daily/Weekly/Monthly)
            reminder_offset: When to show reminder (None/1 day/1 hour/At due)

        Returns:
            The created Task object

        Raises:
            ValueError: If title is empty, date format invalid, or invalid pattern/offset
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        if due_date and not _validate_date_format(due_date):
            raise ValueError("Invalid date format. Use YYYY-MM-DD")

        if recurrence_pattern not in RECURRENCE_PATTERNS:
            recurrence_pattern = "None"

        if reminder_offset not in REMINDER_OFFSETS:
            reminder_offset = "None"

        task = Task(
            id=self.next_id,
            user_id=user_id,
            title=title.strip(),
            description=description.strip() if description else "",
            completed=False,
            priority=priority,
            category=category,
            due_date=due_date.strip() if due_date else "",
            updated_flag=False,
            recurrence_pattern=recurrence_pattern,
            reminder_offset=reminder_offset,
            reminder_shown=False
        )
        self.tasks.append(task)
        self.next_id += 1
        return task

    def list_tasks(self) -> List[Task]:
        """Return all tasks.

        Returns:
            List of all Task objects, in creation order
        """
        return self.tasks.copy()

    def get_task(self, task_id: int) -> Optional[Task]:
        """Retrieve a task by its ID.

        Args:
            task_id: The unique identifier of the task

        Returns:
            The Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by its ID.

        Args:
            task_id: The unique identifier of the task to delete

        Returns:
            True if the task was deleted, False if not found
        """
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                return True
        return False

    def toggle_complete(self, task_id: int) -> Tuple[Task, Optional[Task]]:
        """Toggle the completion status of a task.

        If completing a recurring task, automatically creates the next instance.

        Args:
            task_id: The unique identifier of the task

        Returns:
            Tuple of (updated task, new recurring task or None)

        Raises:
            ValueError: If task_id does not exist
        """
        task = self.get_task(task_id)
        if task is None:
            raise ValueError(f"Task with ID {task_id} not found")

        task.completed = not task.completed
        new_task = None

        # If completing a recurring task, create next instance
        if task.completed and task.recurrence_pattern != "None" and task.due_date:
            next_due = _calculate_next_due_date(task.due_date, task.recurrence_pattern)
            if next_due:
                new_task = self.add_task(
                    user_id=task.user_id,
                    title=task.title,
                    description=task.description,
                    priority=task.priority,
                    category=task.category,
                    due_date=next_due,
                    recurrence_pattern=task.recurrence_pattern,
                    reminder_offset=task.reminder_offset
                )

        return task, new_task

    def search_tasks(self, keyword: str) -> List[Task]:
        """Search tasks by keyword in title, description, and recurrence pattern.

        Args:
            keyword: The search keyword (case-insensitive)

        Returns:
            List of Task objects matching the keyword
        """
        if not keyword:
            return self.tasks.copy()

        keyword_lower = keyword.lower()
        return [
            task for task in self.tasks
            if (keyword_lower in task.title.lower() or
                keyword_lower in task.description.lower() or
                keyword_lower in task.recurrence_pattern.lower())
        ]

    def filter_tasks(
        self,
        status: str = "All",
        priority: str = "All",
        category: str = "All",
        recurrence: str = "All",
        overdue: str = "All"
    ) -> List[Task]:
        """Filter tasks by status, priority, category, recurrence, and/or overdue.

        Args:
            status: Filter by status (All/Pending/Completed)
            priority: Filter by priority (All/High/Medium/Low)
            category: Filter by category (All/Work/Home/Personal)
            recurrence: Filter by recurrence (All/None/Daily/Weekly/Monthly)
            overdue: Filter by overdue status (All/Overdue/Not Overdue)

        Returns:
            List of Task objects matching all filter criteria (AND logic)
        """
        filtered = self.tasks

        # Filter by status
        if status == "Pending":
            filtered = [t for t in filtered if not t.completed]
        elif status == "Completed":
            filtered = [t for t in filtered if t.completed]

        # Filter by priority
        if priority != "All":
            filtered = [t for t in filtered if t.priority == priority]

        # Filter by category
        if category != "All":
            filtered = [t for t in filtered if t.category == category]

        # Filter by recurrence pattern
        if recurrence != "All":
            filtered = [t for t in filtered if t.recurrence_pattern == recurrence]

        # Filter by overdue status
        if overdue == "Overdue":
            filtered = [t for t in filtered if self.is_overdue(t)]
        elif overdue == "Not Overdue":
            filtered = [t for t in filtered if not self.is_overdue(t)]

        return filtered

    def sort_tasks(self, tasks: List[Task], sort_by: str = "date", direction: str = "desc") -> List[Task]:
        """Sort tasks by the specified criteria.

        Args:
            tasks: List of tasks to sort
            sort_by: Sort field (date/priority/alpha/due)
            direction: Sort direction (asc/desc)

        Returns:
            Sorted list of Task objects
        """
        sorted_tasks = tasks.copy()

        if sort_by == "priority":
            # Priority order: High -> Medium -> Low
            priority_order = {"High": 0, "Medium": 1, "Low": 2}
            sorted_tasks.sort(key=lambda t: priority_order.get(t.priority, 3))
            if direction == "desc":
                sorted_tasks.reverse()
        elif sort_by == "alpha":
            sorted_tasks.sort(key=lambda t: t.title.lower())
            if direction == "desc":
                sorted_tasks.reverse()
        elif sort_by == "due":
            # Sort by due date (tasks without due date go to end)
            def due_key(t: Task) -> str:
                return t.due_date if t.due_date else "9999-99-99"
            sorted_tasks.sort(key=due_key, reverse=(direction == "desc"))
        else:  # date (default)
            # Sort by ID descending (newest first)
            sorted_tasks.sort(key=lambda t: t.id, reverse=(direction == "desc"))

        return sorted_tasks

    def update_task(
        self,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
        priority: Optional[str] = None,
        category: Optional[str] = None,
        due_date: Optional[str] = None,
        recurrence_pattern: Optional[str] = None,
        reminder_offset: Optional[str] = None
    ) -> Task:
        """Update an existing task's fields.

        Args:
            task_id: The unique identifier of the task to update
            title: New title for the task (optional)
            description: New description for the task (optional)
            priority: New priority for the task (optional)
            category: New category for the task (optional)
            due_date: New due date for the task (optional, YYYY-MM-DD format)
            recurrence_pattern: New recurrence pattern (optional)
            reminder_offset: New reminder offset (optional)

        Returns:
            The updated Task object

        Raises:
            ValueError: If task_id does not exist, title is empty, or date format invalid
        """
        task = self.get_task(task_id)
        if task is None:
            raise ValueError(f"Task with ID {task_id} not found")

        if title is not None:
            if not title.strip():
                raise ValueError("Task title cannot be empty")
            task.title = title.strip()

        if description is not None:
            task.description = description.strip()

        if priority is not None:
            task.priority = priority

        if category is not None:
            task.category = category

        if due_date is not None:
            if due_date and not _validate_date_format(due_date):
                raise ValueError("Invalid date format. Use YYYY-MM-DD")
            task.due_date = due_date.strip() if due_date else ""

        if recurrence_pattern is not None:
            if recurrence_pattern in RECURRENCE_PATTERNS:
                task.recurrence_pattern = recurrence_pattern

        if reminder_offset is not None:
            if reminder_offset in REMINDER_OFFSETS:
                task.reminder_offset = reminder_offset
                # Reset reminder_shown when offset changes
                task.reminder_shown = False

        # Set updated flag if any field was changed
        if any(arg is not None for arg in [title, description, priority, category, due_date, recurrence_pattern, reminder_offset]):
            task.updated_flag = True

        return task
