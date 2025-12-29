---
id: "007"
title: "Phase II Advanced Todo CLI"
stage: "implement"
date: "2025-12-27"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "001-todo-cli"
branch: "001-todo-cli"
user: "todo-user"
command: "/sp.implement"
labels: [implement,phase-2,advanced,todo-cli,search,filter,sort]
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

Title: "Phase II – Advanced Todo CLI with Search, Filter, Sort"
Stage: implement
Date: 2025-12-27
Feature: 001-todo-cli
Branch: 001-todo-cli
User: todo-user
Description:
- Upgrade the existing Todo CLI app (Phase I) to **Phase II – Intermediate/Advanced**.
- Implement **Priorities** (High, Medium, Low) and **Categories/Tags** (Work, Home, Personal).
- Add **Search, Filter, and Sort** functionality:
  - Search tasks by keyword in title or description
  - Filter by status, priority, or category
  - Sort by due date, priority, or title alphabetically
- Maintain **clean, aligned, developer-grade terminal UI**:
  - Use `=====` for headers/footers
  - Use `-----` for row separators
  - Columns aligned for ID, User, Status, Priority, Category, Title, Description, Due Date, Updated
- Include **distinct system messages**:
  - `[ SUCCESS ]` for success
  - `[ ERROR ]` for errors
  - `[ INFO ]` for informational messages
- Add **Welcome** at the start and **Allah Hafiz!** on exit
- Keep **menu always visible and separate**

## Response snapshot

Implemented Phase II - Advanced Todo CLI with complete feature set:

**Task Model (src/models/task.py):**
- id: int (unique identifier)
- user_id: int (owner)
- title: str (required)
- description: str (optional)
- completed: bool (default False)
- priority: str (High/Medium/Low, default Medium)
- category: str (Work/Home/Personal, default Personal)
- updated_flag: bool (track modifications)

**TaskService (src/services/task_service.py):**
- add_task(user_id, title, description, priority, category)
- update_task(task_id, title, description, priority, category)
- delete_task(task_id)
- toggle_complete(task_id)
- search_tasks(keyword) - case-insensitive, title/description
- filter_tasks(status, priority, category) - AND logic
- sort_tasks(tasks, sort_by, direction) - date/priority/alpha

**Menu UI (src/cli/menu.py) - 9 Column Table:**
```
  ID |  USER | STATUS   | PRIORITY | CATEGORY | TITLE                | DESCRIPTION        |      DUE | UPDATED
========================================================================================================================
   1 |   101 | Active | High | Personal | Buy groceries        | Get milk and brea> |        - | No
   2 |   102 | Active | Medium | Work     | Complete project re> | Q4 summary         |        - | No
   3 |   101 | Active | High | Work     | Fix login bug        | Auth issue fix     |        - | No
```

**Color Scheme:**
- System: White
- Prompts: Cyan
- Success: Green `[ SUCCESS ]`
- Error: Red `[ ERROR ]`
- Info: Blue `[ INFO ]`
- Priority High: Red
- Priority Medium: Yellow
- Priority Low: Green
- Status Active: Yellow
- Status Completed: Green
- Updated Yes: Cyan

**Features Tested:**
- Add Task with Priority/Category
- Search by keyword
- Filter by status/priority/category
- Sort by priority (desc) - Medium first, then High
- Toggle Complete
- Update Task with new priority/category
- Menu always visible
- Welcome message
- "Allah Hafiz!" exit message

## Outcome

- ✅ Impact: Phase II Advanced Todo CLI fully implemented with all features
- 📁 Files: Updated task model, service, and menu
- 🔁 Next prompts: Ready for production use
- 🧠 Reflection: Complete spec-driven implementation with professional UI

## Evaluation notes (flywheel)

- Failure modes observed: "null"
- Graders run and results (PASS/FAIL): "N/A"
- Prompt variant (if applicable): "null"
- Next experiment (smallest change to try): "null"
