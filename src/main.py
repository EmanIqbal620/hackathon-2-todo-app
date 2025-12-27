"""Entry point for the Todo CLI application."""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from services.task_service import TaskService
from cli.menu import Menu


def main() -> None:
    """Start the Todo CLI application."""
    task_service = TaskService()
    menu = Menu(task_service)
    menu.run()


if __name__ == "__main__":
    main()
