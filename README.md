# In-Memory Python CLI Todo Application

A terminal-based todo application built with Python 3.13+ following spec-driven development principles.

## Features

- **Add Task**: Create new tasks with title and optional description
- **View Tasks**: List all tasks with their completion status
- **Update Task**: Modify task title and/or description
- **Delete Task**: Remove tasks by ID
- **Toggle Complete**: Mark tasks as complete/incomplete

## Requirements

- Python 3.13 or higher
- colorama (for colored terminal output)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd todo-app
   ```

2. Install dependencies:
   ```bash
   pip install colorama
   ```

   Or using UV:
   ```bash
   uv pip install colorama
   ```

## Usage

Run the application:
```bash
python src/main.py
```

### Menu Options

1. **Add Task** - Create a new task with title and optional description
2. **View Tasks** - Display all tasks with status (✔ for complete, ✖ for incomplete)
3. **Update Task** - Modify an existing task by ID
4. **Delete Task** - Remove a task by ID
5. **Toggle Complete** - Switch a task's completion status
6. **Exit** - Close the application

## Project Structure

```
todo-app/
├── src/
│   ├── __init__.py
│   ├── main.py              # Application entry point
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py          # Task dataclass
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_service.py  # Task CRUD operations
│   └── cli/
│       ├── __init__.py
│       └── menu.py          # Menu interface
├── specs/
│   └── 001-todo-cli/
│       ├── spec.md          # Feature specification
│       ├── plan.md          # Implementation plan
│       └── tasks.md         # Task list
├── .specify/
│   ├── memory/
│   │   └── constitution.md  # Project constitution
│   └── templates/           # Spec-Kit Plus templates
├── CLAUDE.md                # Claude Code instructions
└── README.md                # This file
```

## Development

This project follows spec-driven development using Spec-Kit Plus:

1. **Constitution** (`.specify/memory/constitution.md`) - Core principles and standards
2. **Specification** (`specs/001-todo-cli/spec.md`) - Feature requirements
3. **Plan** (`specs/001-todo-cli/plan.md`) - Architecture and technical decisions
4. **Tasks** (`specs/001-todo-cli/tasks.md`) - Implementation task list

## License

MIT
"# hackathon-2-todo-app" 
