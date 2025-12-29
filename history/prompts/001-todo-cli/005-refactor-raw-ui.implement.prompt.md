---
id: "005"
title: "Refactor Raw Column-Based UI"
stage: "implement"
date: "2025-12-27"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "001-todo-cli"
branch: "001-todo-cli"
user: "todo-user"
command: "/sp.implement"
labels: [implement,refactor,ui,todo-cli,column-based]
links:
  spec: "null"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
  - "src/cli/menu.py"
tests: []
---

## Prompt

/sp.implement
Title: "Refactor Todo CLI UI to Raw Column-Based Layout"
Stage: implement
Feature: 001-todo-cli
Branch: 001-todo-cli

Goal:
Refactor the existing Todo CLI UI to a clean, raw, professional,
developer-style layout using rows and columns only.

UI Rules:
- Do NOT use Unicode box characters (╔ ║ ╚ etc)
- Do NOT use mixed +---+ style borders
- Use "=" for section headers
- Use "-" for row separators
- Use fixed-width columns for task display
- Keep UI consistent across all screens

Task Table Format:
Columns:
ID | USER | STATUS | PRIORITY | CATEGORY | TITLE | DESCRIPTION | DUE

Requirements:
- All task listings must be shown in a single aligned table
- Search, filter, and sort outputs must reuse the same table format
- Feedback and errors must appear as single-line messages between separators
- Welcome and exit messages must use "=" separators
- No decorative boxes, only clean lines

Success Criteria:
- Output looks clean, aligned, and readable in any terminal
- No broken borders or misaligned

## Response snapshot

Refactored `src/cli/menu.py` from boxed UI to raw column-based layout:

**Changes Made:**
- Removed all box drawing characters (+, -, |)
- Added `COLUMNS` dict with fixed-width column definitions
- Added `_print_header()` method using `=` separators
- Added `_print_separator()` method using `-` or `=` characters
- Added `_format_task_row()` method for consistent row formatting
- Updated `_display_tasks_list()` to show aligned table with 8 columns
- Updated `_display_welcome()` and `_display_exit()` with `=` headers
- Updated `_show_feedback()` to single-line format between separators
- Updated all search/filter/sort handlers to reuse table format
- Color-coded priorities preserved (High=Red, Medium=Yellow, Low=Green)

**New UI Format:**
```
============================================================
 WELCOME TO TODO CLI APP
============================================================

Manage your tasks efficiently

============================================================
 TASKS LIST
============================================================

  ID |  USER |  STATUS | PRIORITY | CATEGORY | TITLE                     | DESCRIPTION                    |        DUE
============================================================
   1 |   101 | pend | High | Personal | Buy groceries             | Get milk and bread             |          -
   2 |   102 | pend | Medium |     Work | Complete project report   | Q4 summary document            |          -
   3 |   103 | pend | Low | Personal | Review pull requests      | Check code changes             |          -

============================================================
 TODO MENU
============================================================

1. Add Task
...
9. Exit

============================================================
 EXIT
============================================================

Allah Hafiz!
```

## Outcome

- ✅ Impact: Refactored Todo CLI UI to clean, raw column-based professional layout
- 📁 Files: Updated `src/cli/menu.py`
- 🔁 Next prompts: Test search, filter, sort functionality
- 🧠 Reflection: New UI is cleaner and more developer-friendly

## Evaluation notes (flywheel)

- Failure modes observed: "null"
- Graders run and results (PASS/FAIL): "N/A"
- Prompt variant (if applicable): "null"
- Next experiment (smallest change to try): "null"
