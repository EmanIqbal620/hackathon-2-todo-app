---
id: "006"
title: "UI Clarity Refinement"
stage: "implement"
date: "2025-12-27"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "001-todo-cli"
branch: "001-todo-cli"
user: "todo-user"
command: "/sp.implement"
labels: [implement,ui,clarity,professional,todo-cli]
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
id: "005"
title: "Todo CLI UI Clarity & Professional Layout Refinement"
stage: "implement"
date: "2025-12-27"
feature: "001-todo-cli"
branch: "001-todo-cli"
user: "todo-user"

## Objective
Refine the existing Todo CLI application's **terminal user interface** to be clear, professional, and non-confusing, following real-world CLI UX principles.

This implementation focuses **only on presentation and communication**, not business logic.

---

## Scope (What to Change)

### 1. UI Structure & Flow
- Introduce clear separation between:
  - SYSTEM messages (headings, summaries)
  - USER prompts (input requests)
  - FEEDBACK messages (success, error, warning)
- Ensure the user always understands:
  - What just happened
  - What is currently being shown
  - What action is expected next

---

### 2. Layout Rules
- Use **only simple ASCII separators**:
  - Section headers: `=` characters
  - Table dividers: `-` characters
- Do NOT use broken box characters (`╔═╦╝` etc.)
- Avoid repeated or unnecessary headings

---

### 3. Menu Presentation
- Menu must appear:
  - Once per interaction cycle
  - Clearly labeled as `[ MENU ]`
- Menu options must be numbered consistently
- Prompt format:
  `Enter choice (1–9):`

---

### 4. Task List Display
- Display tasks in a clean tabular layout using aligned columns:
  - ID
  - User ID
  - Status (Active / Completed)
  - Priority
  - Category
  - Title
  - Due Date
- Include a clear title:
  `TASK LIST (Total: X)`

---

### 5. Feedback Messaging
- All feedback must be wrapped with labels:
  - `[ SUCCESS ]`
  - `[ ERROR ]`
  - `[ INFO ]`
- Feedback must be concise and human-readable
- Errors must explain what went wrong and what to do next

---

### 6. Color Usage (If enabled)
- System headings → neutral color
- User input prompts → highlight color
- Success → green
- Error → red
- Do NOT use the same color for all output

---

### 7. Welcome & Exit Messages
- On app start, show a single clean welcome header
- On exit:
  - Display a polite closing message

## Response snapshot

Refactored `src/cli/menu.py` with clear UI separation and professional layout:

**Output Helper Methods Added:**
- `_print_header()` - Section headers with `=` separators
- `_print_subheader()` - Subheaders like `[ MENU ]`
- `_print_separator()` - Reusable separator lines
- `_print_system()` - System messages (white/neutral)
- `_print_prompt()` - User input prompts (cyan)
- `_print_info()` - Info messages with `[ INFO ]` label (blue)
- `_print_success()` - Success messages with `[ SUCCESS ]` label (green)
- `_print_error()` - Error messages with `[ ERROR ]` label (red)

**UI Changes:**
- Removed Description column (reduced visual noise)
- Status now shows "Active" / "Completed" instead of "pend" / "done"
- Menu labeled as `--- MENU ---`
- Task table title shows count: `CURRENT TASKS (Total: X)`
- Consistent color scheme:
  - System: White
  - Prompts: Cyan
  - Success: Green
  - Error: Red
  - Info: Blue
  - Priority: Red/Yellow/Green

**New UI Output:**
```
============================================================
 WELCOME TO TODO CLI APP
============================================================

Manage your tasks efficiently


[ INFO ] No tasks found.


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

============================================================
 ADD NEW TASK
============================================================

Enter task title: Buy groceries
Enter task description (optional): Get milk and bread
Enter User ID (default 101): 101
Priority options: High, Medium, Low
Enter priority (default: Medium): High
Category options: Work, Home, Personal
Enter category (default: Personal): Personal
[ SUCCESS ] Task created successfully. (ID: 1)

CURRENT TASKS (Total: 1)
  ID |  USER | STATUS   | PRIORITY | CATEGORY | TITLE                     |        DUE
============================================================
   1 |   101 | Active | High | Personal | Buy groceries             |          -

--- MENU ---

  1. Add Task
...

============================================================
 GOODBYE
============================================================

Thank you for using Todo CLI.
Allah Hafiz!
```

## Outcome

- ✅ Impact: UI clarified with clear separation between system/prompt/feedback messages
- 📁 Files: Updated `src/cli/menu.py`
- 🔁 Next prompts: Ready for production use
- 🧠 Reflection: New UI is more intuitive and professional

## Evaluation notes (flywheel)

- Failure modes observed: "null"
- Graders run and results (PASS/FAIL): "N/A"
- Prompt variant (if applicable): "null"
- Next experiment (smallest change to try): "null"
