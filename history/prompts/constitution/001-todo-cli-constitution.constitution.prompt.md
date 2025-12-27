---
id: "001"
title: "Todo CLI App Constitution"
stage: "constitution"
date: "2025-12-27"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "none"
branch: "master"
user: "todo-user"
command: "/sp.constitution"
labels: [constitution,project-setup,todo-app]
links:
  spec: "null"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
  - ".specify/memory/constitution.md"
tests: []
---

## Prompt

# Constitution – Todo CLI App (Phase I)

## Project
Todo In-Memory Python Console Application
**Objective:** Build a terminal-based todo app using spec-driven development (Spec-Kit Plus and Claude Code) that manages tasks entirely in memory.

## Core Principles
- **Accuracy:** All task operations must work exactly as specified (Add, List, Update, Delete, Toggle Complete).
- **Clarity:** Code should be clean, readable, and maintainable; variable and function names must reflect purpose clearly.
- **Reproducibility:** Results of all actions (adding, updating, deleting, toggling tasks) must be consistent across sessions.
- **Rigor:** Application strictly follows the spec; no extra features, no database, no external APIs.

## Key Standards
- Python version: **3.13+**
- Storage: **In-memory only** (list of tasks)
- CLI-only interface; must be menu-driven
- Task Model Fields: `id` (int), `title` (string), `description` (string), `completed` (bool)
- Menu Options: Add, List, Update, Delete, Toggle Complete
- UI: Colored terminal output using **colorama**; symbols ✔ / ✖ for completion
- All code must adhere to clean code principles; no unused code or features
- No persistence of tasks between runs

## Constraints
- **Prohibited Features:** Authentication, categories, priorities, due dates, database or file storage, GUI
- **Execution Environment:** Terminal only (no web, no GUI frameworks)
- Must follow spec-driven development strictly using Claude Code and Spec-Kit Plus

## Success Criteria
- All 5 basic features implemented correctly
- Menu interface works and validates user input
- Task operations correctly handle invalid input (e.g., non-existent ID, empty title)
- Terminal output is clear, readable, and uses color to highlight status
- Fully runs in terminal without errors
- Project structure matches deliverables:

## Response snapshot

Created project constitution at `.specify/memory/constitution.md` with:
- 5 core principles: Accuracy, Clarity, Reproducibility, Rigor (NON-NEGOTIABLE), Simplicity
- Key Standards section documenting Python 3.13+, in-memory storage, colorama UI
- Constraints section listing prohibited features (auth, categories, priorities, due dates, persistence, GUI)
- Success Criteria section with measurable outcomes
- Governance section with amendment procedure, compliance expectations, and versioning policy
- Sync Impact Report embedded as HTML comment at top of file
- Version: 1.0.0 (new constitution, ratified and last amended 2025-12-27)

## Outcome

- ✅ Impact: Project constitution established for Todo CLI App
- 📁 Files: `.specify/memory/constitution.md`
- 🔁 Next prompts: `/sp.spec` to create feature specification
- 🧠 Reflection: Constitution sets clear boundaries preventing scope creep; "Rigor" principle explicitly prohibits extra features

## Evaluation notes (flywheel)

- Failure modes observed: "null"
- Graders run and results (PASS/FAIL): "N/A"
- Prompt variant (if applicable): "null"
- Next experiment (smallest change to try): "null"
