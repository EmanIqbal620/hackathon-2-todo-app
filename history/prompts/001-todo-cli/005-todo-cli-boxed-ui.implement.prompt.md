---
id: "005"
title: "Todo CLI Boxed UI Implementation"
stage: "implement"
date: "2025-12-27"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "001-todo-cli"
branch: "001-todo-cli"
user: "todo-user"
command: "/sp.implement"
labels: [boxed-ui,colorama,cli,todo-app,phase-1]
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

---
id: "005"
title: "Todo CLI Boxed UI Implementation"
stage: "implement"
date: "2025-12-27"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "001-todo-cli"
branch: "001-todo-cli"
user: "todo-user"
---

## Objective
Enhance the completed Todo CLI app (Phase I) with a **professional boxed terminal UI** using Spec-Kit Plus.

### Requirements
1. Welcome message at start.
2. Tasks List in a box with:
   - Task ID
   - User ID
   - Title
   - Description
   - Completion status ([X]/[ ]) with colors.
3. Todo Menu in a box with options 1-6.
4. Feedback messages in a box after actions (Add, Update, Delete, Toggle).
5. Tasks List refresh automatically after every action.
6. Exit message: "Allah Hafiz".
7. Colors via `colorama`.
8. Box-drawing characters (`+`, `-`, `|`).
9. Preserve all Phase I features (Add, Update, Delete, Toggle, View).

### Success Criteria
- All Phase I features fully functional.
- Tasks List & Menu in boxed format.
- Colors clearly show completed/incomplete tasks.
- User IDs displayed.
- Feedback messages appear in boxes.
- Exits cleanly with "Allah Hafiz".

## Response snapshot

Implemented boxed UI enhancement for Todo CLI app:

**Changes Made:**
- Added `user_id` field to Task model
- Updated TaskService.add_task() to accept user_id parameter
- Created _print_box() helper method for box rendering
- Implemented _display_welcome() with "Welcome to Todo CLI App" box
- Implemented _display_tasks_list() with Task ID, User ID, title, description, status
- Implemented _display_main_menu() with boxed menu options
- Implemented _show_feedback() for action feedback in boxes
- Implemented _display_exit() with "Allah Hafiz" message
- Tasks list auto-refreshes after every action
- Used ASCII-safe box characters for Windows compatibility

**UI Structure:**
```
+-- Welcome to Todo CLI App ----------------------+
| Manage your tasks efficiently                    |
+------------------------------------------------+
+-- Tasks List -----------------------------------+
| [ ] Task ID:1 | User ID:101 - Hackathon 2       |
|   Description: Phase 2                          |
+------------------------------------------------+
+-- Todo Menu --------------------------+
| 1. Add Task                            |
| 2. View Tasks                          |
| ...                                    |
+--------------------------------------+
Enter your choice (1-6):

+-- Feedback -------------------------------------+
| Task added successfully! (ID: 1)                |
+------------------------------------------------+

+--------------------+
|                    |
|   Allah Hafiz!      |
|                    |
+--------------------+
```

## Outcome

- ✅ Impact: Boxed UI with all features working
- 📁 Files: 3 files modified (task.py, task_service.py, menu.py)
- 🧠 Reflection: Auto-refresh tasks list provides better UX; ASCII boxes ensure cross-platform compatibility

## Evaluation notes (flywheel)

- Failure modes observed: "null"
- Graders run and results (PASS/FAIL): "N/A"
- Prompt variant (if applicable): "null"
- Next experiment (smallest change to try): "null"
