"""Professional Todo CLI with clean terminal UI."""

from colorama import Fore, Style, init
from services.task_service import TaskService
from services.reminder_service import ReminderService
from models.task import PRIORITY_LEVELS, CATEGORY_OPTIONS, RECURRENCE_PATTERNS, REMINDER_OFFSETS

# Initialize colorama for cross-platform colored output
init(autoreset=True)


class Menu:
    """Professional Todo CLI Menu with clean, aligned UI."""

    # Fixed width for the UI
    WIDTH = 62

    # Color scheme
    COLORS = {
        "header": Fore.CYAN,
        "border": Fore.BLUE,
        "section": Fore.YELLOW,
        "menu_num": Fore.CYAN,
        "menu_text": Fore.WHITE,
        "prompt": Fore.GREEN,
        "table_head": Fore.YELLOW,
        "id": Fore.CYAN,
        "title": Fore.WHITE,
        "desc": Fore.LIGHTBLACK_EX,
        "completed": Fore.GREEN,
        "pending": Fore.YELLOW,
        "overdue": Fore.RED,
        "success": Fore.GREEN,
        "error": Fore.RED,
        "info": Fore.CYAN,
        "option": Fore.MAGENTA,
        "label": Fore.LIGHTBLACK_EX,
    }

    def __init__(self, task_service: TaskService) -> None:
        """Initialize the menu with a task service."""
        self.task_service = task_service
        self.reminder_service = ReminderService()
        self.current_user_id = 101

    # =========================================================================
    # UI BUILDING BLOCKS
    # =========================================================================

    def _line(self, char: str = "─") -> str:
        """Return a horizontal line."""
        return f"{self.COLORS['border']}{char * self.WIDTH}{Style.RESET_ALL}"

    def _double_line(self) -> str:
        """Return a double horizontal line."""
        return f"{self.COLORS['border']}{'═' * self.WIDTH}{Style.RESET_ALL}"

    def _box_top(self) -> str:
        """Return top border of a box."""
        return f"{self.COLORS['border']}╔{'═' * (self.WIDTH - 2)}╗{Style.RESET_ALL}"

    def _box_bottom(self) -> str:
        """Return bottom border of a box."""
        return f"{self.COLORS['border']}╚{'═' * (self.WIDTH - 2)}╝{Style.RESET_ALL}"

    def _box_middle(self, text: str, color=None) -> str:
        """Return a box row with centered text."""
        c = color or self.COLORS['header']
        reset = Style.RESET_ALL
        border = self.COLORS['border']
        inner_width = self.WIDTH - 4
        centered = text.center(inner_width)
        return f"{border}║{reset} {c}{Style.BRIGHT}{centered}{reset} {border}║{reset}"

    def _section_header(self, title: str) -> None:
        """Print a section header with decorative line."""
        c = self.COLORS
        reset = Style.RESET_ALL
        print()
        print(f"{c['section']}{Style.BRIGHT}┌─ {title} {'─' * (self.WIDTH - len(title) - 4)}┐{reset}")

    def _section_footer(self) -> None:
        """Print a section footer."""
        c = self.COLORS
        reset = Style.RESET_ALL
        print(f"{c['section']}└{'─' * (self.WIDTH - 2)}┘{reset}")

    # =========================================================================
    # MESSAGE OUTPUT
    # =========================================================================

    def _print_success(self, message: str) -> None:
        """Print success message."""
        c = self.COLORS
        reset = Style.RESET_ALL
        print()
        print(f"  {c['success']}{Style.BRIGHT}✓ SUCCESS{reset}  {c['menu_text']}{message}{reset}")
        print()

    def _print_updated(self, message: str) -> None:
        """Print update message."""
        c = self.COLORS
        reset = Style.RESET_ALL
        print()
        print(f"  {c['info']}{Style.BRIGHT}↻ UPDATED{reset}   {c['menu_text']}{message}{reset}")
        print()

    def _print_completed(self, message: str) -> None:
        """Print completed message."""
        c = self.COLORS
        reset = Style.RESET_ALL
        print()
        print(f"  {c['completed']}{Style.BRIGHT}✓ COMPLETED{reset} {c['menu_text']}{message}{reset}")
        print()

    def _print_deleted(self, message: str) -> None:
        """Print deleted message."""
        c = self.COLORS
        reset = Style.RESET_ALL
        print()
        print(f"  {c['error']}{Style.BRIGHT}✕ DELETED{reset}   {c['menu_text']}{message}{reset}")
        print()

    def _print_pending(self, message: str) -> None:
        """Print pending message."""
        c = self.COLORS
        reset = Style.RESET_ALL
        print()
        print(f"  {Fore.YELLOW}{Style.BRIGHT}○ PENDING{reset}   {c['menu_text']}{message}{reset}")
        print()

    def _print_error(self, message: str) -> None:
        """Print error message."""
        c = self.COLORS
        reset = Style.RESET_ALL
        print()
        print(f"  {c['error']}{Style.BRIGHT}✕ ERROR{reset}     {c['error']}{message}{reset}")
        print()

    def _print_info(self, message: str) -> None:
        """Print info message."""
        c = self.COLORS
        reset = Style.RESET_ALL
        print()
        print(f"  {c['info']}{Style.BRIGHT}ℹ INFO{reset}      {c['menu_text']}{message}{reset}")
        print()

    def _print_reminder(self, task) -> None:
        """Print a reminder notification for a task."""
        c = self.COLORS
        reset = Style.RESET_ALL
        print()
        print(f"  {Fore.MAGENTA}{Style.BRIGHT}🔔 REMINDER{reset}  {c['menu_text']}{self.reminder_service.format_reminder(task)}{reset}")
        print()

    def _prompt(self, message: str) -> str:
        """Print prompt and get input."""
        c = self.COLORS
        reset = Style.RESET_ALL
        return input(f"  {c['prompt']}➤{reset} {c['menu_text']}{message}:{reset} ").strip()

    def _select_option(self, label: str, options: list, default: str) -> str:
        """Display options and get user input. Returns default if invalid."""
        c = self.COLORS
        reset = Style.RESET_ALL
        opts = f"{c['option']}{' | '.join(options)}{reset}"
        label_padded = f"{label:<12}"
        default_hint = f"{c['label']}(default: {default}){reset}"
        value = input(f"  {c['prompt']}{label_padded}:{reset} {opts}  {default_hint}: ").strip()
        # Case-insensitive match
        for opt in options:
            if opt.lower() == value.lower():
                return opt
        return default

    # =========================================================================
    # MAIN HEADER
    # =========================================================================

    def _print_app_header(self) -> None:
        """Print the main application header."""
        c = self.COLORS
        print()
        print(self._box_top())
        print(self._box_middle("TODO APP", c['header']))
        print(self._box_middle("━" * 24, c['border']))
        print(self._box_middle("Manage Your Tasks Efficiently", c['label']))
        print(self._box_bottom())

    # =========================================================================
    # TASK TABLE
    # =========================================================================

    def _display_tasks_table(self) -> None:
        """Display current tasks in a professional table."""
        tasks = self.task_service.list_tasks()
        c = self.COLORS
        reset = Style.RESET_ALL

        print()
        print(f"  {c['section']}{Style.BRIGHT}📋 CURRENT TASKS{reset}")
        print(f"  {self._line()}")

        if not tasks:
            print(f"  {c['desc']}   No tasks yet. Select option 1 to add your first task.{reset}")
            print(f"  {self._line()}")
            return

        # Column widths (adjusted for 6 columns)
        id_w = 4
        title_w = 14
        desc_w = 12
        due_w = 10
        recur_w = 8
        status_w = 12

        # Header row
        print(f"  {c['table_head']}{Style.BRIGHT}"
              f"{'ID':<{id_w}}"
              f"{'Title':<{title_w}}"
              f"{'Description':<{desc_w}}"
              f"{'Due':<{due_w}}"
              f"{'Recur':<{recur_w}}"
              f"{'Status':<{status_w}}"
              f"{reset}")
        print(f"  {c['border']}{'─' * id_w}┬{'─' * title_w}┬{'─' * desc_w}┬{'─' * due_w}┬{'─' * recur_w}┬{'─' * status_w}{reset}")

        # Task rows
        for task in tasks:
            # Truncate long strings
            title = task.title[:title_w-3] + ".." if len(task.title) > title_w-1 else task.title
            desc = task.description[:desc_w-3] + ".." if len(task.description) > desc_w-1 else task.description
            if not desc:
                desc = "—"

            # Due date (show — if empty)
            due = task.due_date if task.due_date else "—"

            # Recurrence pattern (show — if None)
            recur = task.recurrence_pattern if task.recurrence_pattern != "None" else "—"

            # Status with icon and color (overdue check)
            if task.completed:
                status = f"{c['completed']}✓ Done{reset}"
            elif self.task_service.is_overdue(task):
                status = f"{c['overdue']}⚠ Overdue{reset}"
            else:
                status = f"{c['pending']}○ Pending{reset}"

            print(f"  {c['id']}{task.id:<{id_w}}{reset}"
                  f"{c['title']}{title:<{title_w}}{reset}"
                  f"{c['desc']}{desc:<{desc_w}}{reset}"
                  f"{c['desc']}{due:<{due_w}}{reset}"
                  f"{c['option']}{recur:<{recur_w}}{reset}"
                  f"{status}")

        print(f"  {self._line()}")
        print(f"  {c['label']}Total: {len(tasks)} task(s){reset}")

    # =========================================================================
    # MAIN MENU
    # =========================================================================

    def _display_menu(self) -> None:
        """Display the main menu options."""
        c = self.COLORS
        reset = Style.RESET_ALL

        print()
        print(f"  {c['section']}{Style.BRIGHT}📌 MENU{reset}")
        print(f"  {self._line()}")
        print(f"  {c['menu_num']}[1]{reset} {c['menu_text']}Add Task{reset}          {c['menu_num']}[6]{reset} {c['menu_text']}Search Tasks{reset}")
        print(f"  {c['menu_num']}[2]{reset} {c['menu_text']}View Tasks{reset}        {c['menu_num']}[7]{reset} {c['menu_text']}Filter Tasks{reset}")
        print(f"  {c['menu_num']}[3]{reset} {c['menu_text']}Update Task{reset}       {c['menu_num']}[8]{reset} {c['menu_text']}Sort Tasks{reset}")
        print(f"  {c['menu_num']}[4]{reset} {c['menu_text']}Delete Task{reset}       {c['menu_num']}[9]{reset} {c['error']}Exit{reset}")
        print(f"  {c['menu_num']}[5]{reset} {c['menu_text']}Toggle Complete{reset}")
        print(f"  {self._line()}")
        print()

    # =========================================================================
    # ACTION HANDLERS
    # =========================================================================

    def _handle_add_task(self) -> None:
        """Handle Add Task action."""
        self._section_header("ADD NEW TASK")
        print()

        title = self._prompt("Task Title")
        if not title:
            self._print_error("Task title cannot be empty.")
            return

        description = self._prompt("Description (optional)")

        # Simple input fields with options displayed
        priority = self._select_option("Priority", PRIORITY_LEVELS, "Medium")
        category = self._select_option("Category", CATEGORY_OPTIONS, "Personal")

        due_date = self._prompt("Due Date YYYY-MM-DD (optional)")

        recurrence = self._select_option("Recurrence", RECURRENCE_PATTERNS, "None")

        # Prompt for reminder only if due date is set
        reminder_offset = "None"
        if due_date:
            reminder_offset = self._select_option("Reminder", REMINDER_OFFSETS, "None")

        try:
            task = self.task_service.add_task(
                self.current_user_id, title, description, priority, category, due_date,
                recurrence_pattern=recurrence,
                reminder_offset=reminder_offset
            )
            self._print_success(f"Task created successfully (ID: {task.id})")
        except ValueError as e:
            self._print_error(str(e))

    def _handle_view_tasks(self) -> None:
        """Handle View Tasks action."""
        self._display_tasks_table()

    def _handle_update_task(self) -> None:
        """Handle Update Task action."""
        self._section_header("UPDATE TASK")
        print()

        task_id = self._prompt("Task ID to update")
        if not task_id:
            self._print_error("Task ID cannot be empty.")
            return

        try:
            task_id = int(task_id)
        except ValueError:
            self._print_error("Invalid ID. Please enter a number.")
            return

        task = self.task_service.get_task(task_id)
        if task is None:
            self._print_error(f"Task with ID {task_id} not found.")
            return

        c = self.COLORS
        reset = Style.RESET_ALL
        print()
        print(f"    {c['label']}Current values:{reset}")
        print(f"    {c['border']}├─{reset} {c['label']}Title:{reset}      {c['title']}{task.title}{reset}")
        print(f"    {c['border']}├─{reset} {c['label']}Priority:{reset}   {c['option']}{task.priority}{reset}")
        print(f"    {c['border']}├─{reset} {c['label']}Category:{reset}   {c['option']}{task.category}{reset}")
        print(f"    {c['border']}├─{reset} {c['label']}Due Date:{reset}   {c['desc']}{task.due_date or '—'}{reset}")
        print(f"    {c['border']}├─{reset} {c['label']}Recurrence:{reset} {c['option']}{task.recurrence_pattern}{reset}")
        print(f"    {c['border']}└─{reset} {c['label']}Reminder:{reset}   {c['option']}{task.reminder_offset}{reset}")
        print()

        new_title = self._prompt("New Title (enter to keep)")
        new_description = self._prompt("New Description (enter to keep)")

        # Simple input fields (use current values as defaults)
        new_priority = self._select_option("Priority", PRIORITY_LEVELS, task.priority)
        if new_priority == task.priority:
            new_priority = None  # No change

        new_category = self._select_option("Category", CATEGORY_OPTIONS, task.category)
        if new_category == task.category:
            new_category = None  # No change

        new_due_date = self._prompt("New Due Date YYYY-MM-DD (enter to keep)")

        new_recurrence = self._select_option("Recurrence", RECURRENCE_PATTERNS, task.recurrence_pattern)
        if new_recurrence == task.recurrence_pattern:
            new_recurrence = None  # No change

        new_reminder = self._select_option("Reminder", REMINDER_OFFSETS, task.reminder_offset)
        if new_reminder == task.reminder_offset:
            new_reminder = None  # No change

        try:
            self.task_service.update_task(
                task_id,
                title=new_title if new_title else None,
                description=new_description if new_description else None,
                priority=new_priority if new_priority else None,
                category=new_category if new_category else None,
                due_date=new_due_date if new_due_date else None,
                recurrence_pattern=new_recurrence if new_recurrence else None,
                reminder_offset=new_reminder if new_reminder else None
            )
            self._print_updated(f"Task {task_id} updated successfully.")
        except ValueError as e:
            self._print_error(str(e))

    def _handle_delete_task(self) -> None:
        """Handle Delete Task action."""
        self._section_header("DELETE TASK")
        print()

        task_id = self._prompt("Task ID to delete")
        if not task_id:
            self._print_error("Task ID cannot be empty.")
            return

        try:
            task_id = int(task_id)
        except ValueError:
            self._print_error("Invalid ID. Please enter a number.")
            return

        if self.task_service.delete_task(task_id):
            self._print_deleted(f"Task {task_id} deleted successfully.")
        else:
            self._print_error(f"Task with ID {task_id} not found.")

    def _handle_toggle_complete(self) -> None:
        """Handle Toggle Complete action."""
        self._section_header("TOGGLE COMPLETE")
        print()

        task_id = self._prompt("Task ID to toggle")
        if not task_id:
            self._print_error("Task ID cannot be empty.")
            return

        try:
            task_id = int(task_id)
        except ValueError:
            self._print_error("Invalid ID. Please enter a number.")
            return

        try:
            task, new_task = self.task_service.toggle_complete(task_id)
            if task.completed:
                self._print_completed(f"Task {task_id} marked as Completed.")
                if new_task:
                    self._print_info(f"Recurring task created: ID {new_task.id}, Due: {new_task.due_date}")
            else:
                self._print_pending(f"Task {task_id} marked as Pending.")
        except ValueError as e:
            self._print_error(str(e))

    def _handle_search_tasks(self) -> None:
        """Handle Search Tasks action."""
        self._section_header("SEARCH TASKS")
        print()

        keyword = self._prompt("Search keyword")
        if not keyword:
            self._print_error("Keyword cannot be empty.")
            return

        results = self.task_service.search_tasks(keyword)

        c = self.COLORS
        reset = Style.RESET_ALL
        print()
        print(f"  {c['section']}{Style.BRIGHT}🔍 RESULTS FOR: '{keyword}'{reset}")
        print(f"  {self._line()}")

        if not results:
            print(f"  {c['desc']}   No tasks found matching your search.{reset}")
            print(f"  {self._line()}")
            return

        self._display_task_list(results)

    def _handle_filter_tasks(self) -> None:
        """Handle Filter Tasks action."""
        self._section_header("FILTER TASKS")
        print()

        # Simple input filter options
        status = self._select_option("Status", ["All", "Pending", "Completed"], "All")
        priority = self._select_option("Priority", ["All"] + PRIORITY_LEVELS, "All")
        category = self._select_option("Category", ["All"] + CATEGORY_OPTIONS, "All")
        recurrence = self._select_option("Recurrence", ["All"] + RECURRENCE_PATTERNS, "All")
        overdue = self._select_option("Overdue", ["All", "Overdue", "Not Overdue"], "All")

        results = self.task_service.filter_tasks(
            status=status, priority=priority, category=category,
            recurrence=recurrence, overdue=overdue
        )

        # Build filter description
        filters = []
        if status != "All":
            filters.append(status)
        if priority != "All":
            filters.append(priority)
        if category != "All":
            filters.append(category)
        if recurrence != "All":
            filters.append(recurrence)
        if overdue != "All":
            filters.append(overdue)
        filter_desc = " + ".join(filters) if filters else "All"

        c = self.COLORS
        reset = Style.RESET_ALL
        print()
        print(f"  {c['section']}{Style.BRIGHT}🔎 FILTERED: {filter_desc}{reset}")
        print(f"  {self._line()}")

        if not results:
            print(f"  {c['desc']}   No tasks match the filter criteria.{reset}")
            print(f"  {self._line()}")
            return

        self._display_task_list(results)

    def _handle_sort_tasks(self) -> None:
        """Handle Sort Tasks action."""
        self._section_header("SORT TASKS")
        print()

        # Simple input sort options
        sort_by = self._select_option("Sort by", ["date", "priority", "alpha", "due"], "date")
        direction = self._select_option("Direction", ["asc", "desc"], "desc")

        tasks = self.task_service.list_tasks()
        sorted_tasks = self.task_service.sort_tasks(tasks, sort_by=sort_by, direction=direction)

        c = self.COLORS
        reset = Style.RESET_ALL
        print()
        print(f"  {c['section']}{Style.BRIGHT}📊 SORTED BY: {sort_by.upper()} ({direction}){reset}")
        print(f"  {self._line()}")

        if not sorted_tasks:
            print(f"  {c['desc']}   No tasks to sort.{reset}")
            print(f"  {self._line()}")
            return

        self._display_task_list(sorted_tasks)

    def _display_task_list(self, tasks) -> None:
        """Display a list of tasks in table format."""
        c = self.COLORS
        reset = Style.RESET_ALL

        # Column widths (adjusted for 6 columns)
        id_w = 4
        title_w = 14
        desc_w = 12
        due_w = 10
        recur_w = 8
        status_w = 12

        # Header row
        print(f"  {c['table_head']}{Style.BRIGHT}"
              f"{'ID':<{id_w}}"
              f"{'Title':<{title_w}}"
              f"{'Description':<{desc_w}}"
              f"{'Due':<{due_w}}"
              f"{'Recur':<{recur_w}}"
              f"{'Status':<{status_w}}"
              f"{reset}")
        print(f"  {c['border']}{'─' * id_w}┬{'─' * title_w}┬{'─' * desc_w}┬{'─' * due_w}┬{'─' * recur_w}┬{'─' * status_w}{reset}")

        # Task rows
        for task in tasks:
            title = task.title[:title_w-3] + ".." if len(task.title) > title_w-1 else task.title
            desc = task.description[:desc_w-3] + ".." if len(task.description) > desc_w-1 else task.description
            if not desc:
                desc = "—"

            # Due date (show — if empty)
            due = task.due_date if task.due_date else "—"

            # Recurrence pattern (show — if None)
            recur = task.recurrence_pattern if task.recurrence_pattern != "None" else "—"

            # Status with icon and color (overdue check)
            if task.completed:
                status = f"{c['completed']}✓ Done{reset}"
            elif self.task_service.is_overdue(task):
                status = f"{c['overdue']}⚠ Overdue{reset}"
            else:
                status = f"{c['pending']}○ Pending{reset}"

            print(f"  {c['id']}{task.id:<{id_w}}{reset}"
                  f"{c['title']}{title:<{title_w}}{reset}"
                  f"{c['desc']}{desc:<{desc_w}}{reset}"
                  f"{c['desc']}{due:<{due_w}}{reset}"
                  f"{c['option']}{recur:<{recur_w}}{reset}"
                  f"{status}")

        print(f"  {self._line()}")
        print(f"  {c['label']}Found: {len(tasks)} task(s){reset}")

    # =========================================================================
    # MAIN APPLICATION LOOP
    # =========================================================================

    def run(self) -> None:
        """Run the main application loop."""
        self._print_app_header()

        while True:
            # Check and display due reminders
            due_reminders = self.reminder_service.check_due_reminders(self.task_service.list_tasks())
            for task in due_reminders:
                self._print_reminder(task)
                self.reminder_service.mark_reminder_shown(task)

            self._display_tasks_table()
            self._display_menu()

            choice = self._prompt("Enter choice (1-9)")

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
                self._handle_search_tasks()
            elif choice == "7":
                self._handle_filter_tasks()
            elif choice == "8":
                self._handle_sort_tasks()
            elif choice == "9":
                c = self.COLORS
                print()
                print(self._box_top())
                print(self._box_middle("GOODBYE", c['header']))
                print(self._box_middle("━" * 24, c['border']))
                print(self._box_middle("Thank you for using Todo App!", c['success']))
                print(self._box_bottom())
                print()
                break
            else:
                self._print_error("Invalid choice. Please enter 1-9.")
