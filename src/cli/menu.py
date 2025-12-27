"""Menu interface for the Todo CLI application with boxed UI."""

from colorama import Fore, Style, init
from services.task_service import TaskService

# Initialize colorama for cross-platform colored output
init(autoreset=True)

# Box drawing characters (ASCII-safe for Windows)
BOX_HORIZONTAL = "-"
BOX_VERTICAL = "|"
BOX_TOP_LEFT = "+"
BOX_TOP_RIGHT = "+"
BOX_BOTTOM_LEFT = "+"
BOX_BOTTOM_RIGHT = "+"
BOX_T_LEFT = "+"
BOX_T_RIGHT = "+"


class Menu:
    """Handles the menu-driven CLI interface with boxed UI.

    Attributes:
        task_service: The TaskService instance for task operations
        current_user_id: The current user's ID (default 101)
    """

    def __init__(self, task_service: TaskService) -> None:
        """Initialize the menu with a task service.

        Args:
            task_service: The TaskService instance to use for operations
        """
        self.task_service = task_service
        self.current_user_id = 101

    def run(self) -> None:
        """Run the main application loop."""
        self._display_welcome()
        while True:
            self._display_tasks_list()
            self._display_main_menu()
            choice = input(f"{Fore.CYAN}Enter your choice (1-6): {Style.RESET_ALL} ").strip()
            if choice == "1":
                self._handle_add_task()
            elif choice == "2":
                self._handle_view_tasks()
            elif choice == "3":
                self._handle_update_task()
            elif choice == "4":
                self._handle_delete_task()
            elif choice == "5":
                self._handle_toggle_complete()
            elif choice == "6":
                self._display_exit()
                break
            else:
                self._show_feedback("Invalid choice! Please enter 1-6.", error=True)

    def _print_box(self, content: str, title: str = "", width: int = 50) -> None:
        """Print content inside a box with optional title.

        Args:
            content: The content to display inside the box
            title: Optional title to display at the top of the box
            width: Width of the box
        """
        # Top border
        if title:
            print(f"{Fore.CYAN}{BOX_TOP_LEFT}{BOX_HORIZONTAL * 2} {title} {BOX_HORIZONTAL * (width - len(title) - 5)}{BOX_TOP_RIGHT}{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}{BOX_TOP_LEFT}{BOX_HORIZONTAL * (width - 2)}{BOX_TOP_RIGHT}{Style.RESET_ALL}")

        # Content lines
        for line in content.split("\n"):
            print(f"{Fore.CYAN}{BOX_VERTICAL}{Style.RESET_ALL} {line:<{width - 2}} {Fore.CYAN}{BOX_VERTICAL}{Style.RESET_ALL}")

        # Bottom border
        print(f"{Fore.CYAN}{BOX_BOTTOM_LEFT}{BOX_HORIZONTAL * (width - 2)}{BOX_BOTTOM_RIGHT}{Style.RESET_ALL}")

    def _display_welcome(self) -> None:
        """Display the welcome message box."""
        content = "Manage your tasks efficiently"
        self._print_box(content, "Welcome to Todo CLI App", width=50)

    def _display_exit(self) -> None:
        """Display the exit message."""
        print(f"\n{Fore.GREEN}{BOX_TOP_LEFT}{BOX_HORIZONTAL * 20}{BOX_TOP_RIGHT}")
        print(f"{Fore.GREEN}{BOX_VERTICAL}                    {BOX_VERTICAL}")
        print(f"{Fore.GREEN}{BOX_VERTICAL}   Allah Hafiz!      {BOX_VERTICAL}")
        print(f"{Fore.GREEN}{BOX_VERTICAL}                    {BOX_VERTICAL}")
        print(f"{Fore.GREEN}{BOX_BOTTOM_LEFT}{BOX_HORIZONTAL * 20}{BOX_BOTTOM_RIGHT}{Style.RESET_ALL}\n")

    def _display_tasks_list(self) -> None:
        """Display the tasks list in a box."""
        tasks = self.task_service.list_tasks()

        if not tasks:
            content = "No tasks found."
            self._print_box(content, "Tasks List", width=50)
            return

        # Build task list content
        lines = []
        for task in tasks:
            if task.completed:
                status = f"{Fore.GREEN}[X]{Style.RESET_ALL}"
            else:
                status = f"{Fore.RED}[ ]{Style.RESET_ALL}"
            lines.append(f"{status} Task ID:{task.id} | User ID:{task.user_id} - {task.title}")
            if task.description:
                lines.append(f"  Description: {task.description}")

        content = "\n".join(lines)
        self._print_box(content, "Tasks List", width=60)

    def _display_main_menu(self) -> None:
        """Display the main menu in a box."""
        content = (
            "1. Add Task\n"
            "2. View Tasks\n"
            "3. Update Task\n"
            "4. Delete Task\n"
            "5. Toggle Complete\n"
            "6. Exit"
        )
        self._print_box(content, "Todo Menu", width=40)

    def _show_feedback(self, message: str, error: bool = False) -> None:
        """Display a feedback message in a box.

        Args:
            message: The message to display
            error: Whether this is an error message
        """
        color = Fore.RED if error else Fore.GREEN
        content = message
        self._print_box(content, "Feedback", width=50)
        print(f"{color}")

    def _handle_add_task(self) -> None:
        """Handle the Add Task menu option."""
        title = input(f"{Fore.CYAN}Enter task title: {Style.RESET_ALL}").strip()
        if not title:
            self._show_feedback("Error: Task title cannot be empty.", error=True)
            return

        description = input(f"{Fore.CYAN}Enter task description (optional): {Style.RESET_ALL}").strip()
        user_id = input(f"{Fore.CYAN}Enter User ID (default {self.current_user_id}): {Style.RESET_ALL}").strip()

        if user_id:
            try:
                user_id = int(user_id)
            except ValueError:
                user_id = self.current_user_id
        else:
            user_id = self.current_user_id

        task = self.task_service.add_task(user_id, title, description)
        self._show_feedback(f"Task added successfully! (ID: {task.id})")

    def _handle_view_tasks(self) -> None:
        """Handle the View Tasks menu option."""
        tasks = self.task_service.list_tasks()
        if not tasks:
            self._show_feedback("No tasks found.", error=True)
        else:
            self._show_feedback(f"Total tasks: {len(tasks)}")

    def _handle_update_task(self) -> None:
        """Handle the Update Task menu option."""
        task_id = input(f"{Fore.CYAN}Enter task ID to update: {Style.RESET_ALL}").strip()
        if not task_id:
            self._show_feedback("Error: Task ID cannot be empty.", error=True)
            return

        try:
            task_id = int(task_id)
        except ValueError:
            self._show_feedback("Error: Invalid ID. Please enter a number.", error=True)
            return

        task = self.task_service.get_task(task_id)
        if task is None:
            self._show_feedback(f"Error: Task with ID {task_id} not found.", error=True)
            return

        new_title = input(f"{Fore.CYAN}Enter new title (leave empty to keep): {Style.RESET_ALL}").strip()
        new_description = input(f"{Fore.CYAN}Enter new description (leave empty to keep): {Style.RESET_ALL}").strip()

        try:
            self.task_service.update_task(
                task_id,
                title=new_title if new_title else None,
                description=new_description if new_description else None
            )
            self._show_feedback(f"Task {task_id} updated successfully!")
        except ValueError as e:
            self._show_feedback(f"Error: {e}", error=True)

    def _handle_delete_task(self) -> None:
        """Handle the Delete Task menu option."""
        task_id = input(f"{Fore.CYAN}Enter task ID to delete: {Style.RESET_ALL}").strip()
        if not task_id:
            self._show_feedback("Error: Task ID cannot be empty.", error=True)
            return

        try:
            task_id = int(task_id)
        except ValueError:
            self._show_feedback("Error: Invalid ID. Please enter a number.", error=True)
            return

        if self.task_service.delete_task(task_id):
            self._show_feedback(f"Task {task_id} deleted successfully!")
        else:
            self._show_feedback(f"Error: Task with ID {task_id} not found.", error=True)

    def _handle_toggle_complete(self) -> None:
        """Handle the Toggle Complete menu option."""
        task_id = input(f"{Fore.CYAN}Enter task ID to toggle: {Style.RESET_ALL}").strip()
        if not task_id:
            self._show_feedback("Error: Task ID cannot be empty.", error=True)
            return

        try:
            task_id = int(task_id)
        except ValueError:
            self._show_feedback("Error: Invalid ID. Please enter a number.", error=True)
            return

        try:
            task = self.task_service.toggle_complete(task_id)
            status = "completed" if task.completed else "incomplete"
            self._show_feedback(f"Task {task_id} marked as {status}!")
        except ValueError as e:
            self._show_feedback(f"Error: {e}", error=True)
