"""Reminder service for handling task notifications."""

from datetime import datetime, timedelta
from typing import List
from models.task import Task


class ReminderService:
    """Handles reminder checking and notifications for tasks."""

    def check_due_reminders(self, tasks: List[Task]) -> List[Task]:
        """Return tasks that need reminder notification now.

        Args:
            tasks: List of all tasks to check

        Returns:
            List of tasks that have due reminders not yet shown
        """
        due_reminders = []
        for task in tasks:
            if self._is_reminder_due(task):
                due_reminders.append(task)
        return due_reminders

    def _is_reminder_due(self, task: Task) -> bool:
        """Check if a task's reminder time has been reached.

        Args:
            task: The task to check

        Returns:
            True if reminder should be shown, False otherwise
        """
        # Skip if no reminder set, already shown, completed, or no due date
        if (task.reminder_offset == "None" or
            task.reminder_shown or
            task.completed or
            not task.due_date):
            return False

        try:
            due_date = datetime.strptime(task.due_date, "%Y-%m-%d")
            now = datetime.now()

            # Calculate reminder time based on offset
            if task.reminder_offset == "1 day":
                reminder_time = due_date - timedelta(days=1)
            elif task.reminder_offset == "1 hour":
                # Since we only have dates, treat this as same day
                reminder_time = due_date
            elif task.reminder_offset == "At due":
                reminder_time = due_date
            else:
                return False

            # Check if reminder time has passed
            return now >= reminder_time

        except ValueError:
            return False

    def mark_reminder_shown(self, task: Task) -> None:
        """Mark a task's reminder as shown to prevent duplicates.

        Args:
            task: The task to mark
        """
        task.reminder_shown = True

    def format_reminder(self, task: Task) -> str:
        """Format a reminder message for CLI display.

        Args:
            task: The task to format reminder for

        Returns:
            Formatted reminder message string
        """
        return f"Task '{task.title}' is due on {task.due_date}!"
