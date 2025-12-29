---
id: "009"
title: "Phase 2 Intermediate Todo CLI"
stage: "implement"
date: "2025-12-27"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "001-todo-cli"
branch: "001-todo-cli"
user: "todo-user"
command: "/sp.implement"
labels: [implement,phase-2,intermediate,cli,colored-output,todo-cli]
links:
  spec: "null"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
  - "src/models/task.py"
  - "src/services/task_service.py"
  - "src/cli/menu.py"
tests: []
---

## Prompt

/sp.implement
Title: "Intermediate Todo CLI – Phase 2 (Raw CLI, Colored Output, Organized)"
Stage: implement
Date: 2025-12-27
Feature: 001-todo-cli
Branch: 001-todo-cli
User: todo-user
Description:
- Upgrade existing Todo CLI app to Intermediate Level (Phase 2).
- CLI UI uses raw-style separators (=====, -----) instead of boxes for professional appearance.
- Color-coded outputs:
    - Headings & separators: Yellow
    - Menu options: Bright White
    - Task User ID: Cyan
    - Task title & description: White
    - Status Completed: Green
    - Status Pending: Red
    - Success messages: Green
    - Error messages: Red
- Features:
    1. Add Task (with Title, Description, User ID, Priority, Category, Due Date)
    2. View Tasks (shows all tasks in raw, readable format)
    3. Update Task
    4. Delete Task
    5. Toggle Complete
    6. Search Tasks (keyword)
    7. Filter Tasks (by Status, Priority, Category)
    8. Sort Tasks (by Date, Priority, Alphabetically)
    9. Exit (shows Allah Hafiz message)
- Each action shows clear feedback and updates (Success/Error) in proper color.
- Tasks display includes ID, User, Title, Description, Status, Priority, Category, Due, Updated.

## Response snapshot

Implemented Phase 2 - Intermediate Todo CLI with raw CLI style and color-coded output:

**Color Scheme - Phase 2 Specific:**
| Element | Color |
|---------|-------|
| Headings & separators | Yellow |
| Menu options | Bright White |
| Task User ID | Cyan |
| Task title & description | White |
| Status Completed | Green |
| Status Pending | Red |
| Success messages | Green |
| Error messages | Red |
| [ INFO ] | Blue |

**Task Model (src/models/task.py):**
- Added `due_date` field (optional, YYYY-MM-DD format)
- All 9 fields: id, user_id, title, description, completed, priority, category, due_date, updated_flag

**TaskService (src/services/task_service.py):**
- Updated `add_task()` to accept `due_date` parameter
- All CRUD operations support due date

**Menu UI (src/cli/menu.py):**
- 9-column fixed-width table with proper alignment
- Raw separators (===== for headers, ----- for rows)
- Due date displayed in table or "-"

**Professional UI Output:**
```
============================================================================================================
       TODO CLI - INTERMEDIATE (PHASE 2)
============================================================================================================

Organize your tasks with:
- Search, Filter & Sort functionality
- Priority levels & Categories
- Due dates & task tracking

============================================================================================================

--- MENU ---
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Toggle Complete
6. Search Tasks
7. Filter Tasks
8. Sort Tasks
9. Exit

Enter choice (1-9):
============================================================================================================
 ADD NEW TASK
============================================================================================================

Enter task title: Buy groceries
Enter task description (optional): Get milk and bread
Enter User ID (default 101): 101
Priority options: High, Medium, Low
Enter priority (default: Medium): High
Category options: Work, Home, Personal
Enter category (default: Personal): Personal
Enter due date (YYYY-MM-DD or leave empty): 2025-01-15
[ SUCCESS ] Task created successfully. (ID: 1)

CURRENT TASKS (Total: 1)
  ID |  USER | TITLE                  | DESCRIPTION        | STATUS   | PRIORITY | CATEGORY |        DUE | UPDATED
============================================================================================================
   1 | 101 | Buy groceries | Get milk and bread | Pending | High | Personal | 2025-01-15 | No

============================================================================================================
                  GOODBYE
============================================================================================================

Thank you for using Todo CLI!
Allah Hafiz!
```

**Features Tested:**
- Add Task with due date
- Search Tasks (keyword)
- Filter Tasks (Status/Priority/Category)
- Sort Tasks (date/priority/alpha)
- Color-coded status (Green Completed, Red Pending)
- Allah Hafiz exit message

## Outcome

- ✅ Impact: Phase 2 Intermediate Todo CLI with raw CLI, colored output, and due dates
- 📁 Files: Updated task model, service, and menu
- 🔁 Next prompts: Ready for production use
- 🧠 Reflection: Professional raw CLI with clear color coding

## Evaluation notes (flywheel)

- Failure modes observed: "null"
- Graders run and results (PASS/FAIL): "N/A"
- Prompt variant (if applicable): "null"
- Next experiment (smallest change to try): "null"
