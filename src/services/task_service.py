"""Task service for managing todo tasks in memory."""

from typing import List, Optional
from models.task import Task


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

    def add_task(self, user_id: int, title: str, description: str = "") -> Task:
        """Create a new task with auto-incremented ID.

        Args:
            user_id: The user ID who owns this task
            title: Brief description of the task (required)
            description: Detailed information about the task (optional)

        Returns:
            The created Task object

        Raises:
            ValueError: If title is empty or whitespace
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        task = Task(
            id=self.next_id,
            user_id=user_id,
            title=title.strip(),
            description=description.strip() if description else "",
            completed=False
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

    def update_task(
        self,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None
    ) -> Task:
        """Update an existing task's title and/or description.

        Args:
            task_id: The unique identifier of the task to update
            title: New title for the task (optional)
            description: New description for the task (optional)

        Returns:
            The updated Task object

        Raises:
            ValueError: If task_id does not exist or title is empty
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

        return task

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

    def toggle_complete(self, task_id: int) -> Task:
        """Toggle the completion status of a task.

        Args:
            task_id: The unique identifier of the task

        Returns:
            The updated Task object

        Raises:
            ValueError: If task_id does not exist
        """
        task = self.get_task(task_id)
        if task is None:
            raise ValueError(f"Task with ID {task_id} not found")

        task.completed = not task.completed
        return task
