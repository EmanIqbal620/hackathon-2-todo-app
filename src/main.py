"""Entry point for the Todo CLI application."""

import sys
import os
from pathlib import Path

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
    os.system('chcp 65001 > nul 2>&1')

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
