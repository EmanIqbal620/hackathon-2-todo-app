# Implementation Plan: In-Memory Python CLI Todo Application

**Branch**: `001-todo-cli` | **Date**: 2025-12-27 | **Spec**: [spec.md](../spec.md)
**Input**: Feature specification from `/specs/001-todo-cli/spec.md`

## Summary

Build a terminal-based todo application in Python that stores tasks in-memory. The application provides a menu-driven CLI interface with 5 core features: Add Task, View Tasks, Update Task, Delete Task, and Toggle Complete. The architecture follows a simple layered approach with a task model, task service for business logic, and menu interface for user interaction.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: colorama (colored terminal output)
**Storage**: In-memory Python list (no persistence)
**Testing**: Manual validation during development
**Target Platform**: Terminal/Console (cross-platform)
**Project Type**: Single CLI application
**Performance Goals**: Responsive CLI (sub-second operation)
**Constraints**: In-memory only, no database, terminal-only
**Scale/Scope**: Single user, local execution

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Requirement | Compliance |
|-----------|-------------|------------|
| I. Accuracy | Task operations work as specified | ✅ Aligns with feature-by-feature testing |
| II. Clarity | Clean, readable code with clear names | ✅ Follows clean code principles |
| III. Reproducibility | Consistent behavior | ✅ In-memory ensures consistency |
| IV. Rigor | No extra features, no database | ✅ Only 5 core features, no persistence |
| V. Simplicity | Simplest implementation | ✅ Single project, minimal dependencies |

**Result**: All gates pass ✅

## Project Structure

### Documentation (this feature)

```text
specs/001-todo-cli/
├── plan.md              # This file (/sp.plan command output)
├── spec.md              # Feature specification (/sp.spec output)
├── research.md          # Phase 0 output (optional)
├── data-model.md        # Phase 1 output (optional)
└── tasks.md             # Phase 2 output (/sp.tasks command)
```

### Source Code (repository root)

```text
src/
├── __init__.py
├── main.py              # Application entry point
├── models/
│   └── __init__.py
│   └── task.py          # Task dataclass/model
├── services/
│   ├── __init__.py
│   └── task_service.py  # Task operations (CRUD)
└── cli/
    ├── __init__.py
    └── menu.py          # Menu interface and user input
```

**Structure Decision**: Single project with models/services/cli separation for clarity. Task model encapsulates data structure, task service handles business logic, menu handles user interaction.

## Decisions

| Decision | Options | Tradeoffs | Chosen |
|----------|---------|-----------|--------|
| Data storage | In-memory list vs database | In-memory is simple, no persistence; DB adds complexity | In-memory list |
| Task identification | Auto-increment ID vs UUID | Auto-increment simpler, easier to debug; UUID more complex | Auto-increment ID |
| Output style | Plain text vs colored | Colored output more user-friendly, slightly more code | Colored with ✔ / ✖ |
| Feature scope | Only basic features vs extras | MVP is faster and meets Phase I requirements | Only 5 basic features |

## Complexity Tracking

> No constitution violations. All decisions align with principles:
> - In-memory storage matches "Rigor" (no database)
> - Auto-increment ID matches "Simplicity" (simplest approach)
> - Colored output matches "Clarity" (user-friendly)
> - Limited scope matches "Rigor" (no extra features)

## Implementation Phases

### Phase 1: Foundation (Add + View Tasks)

**Goal**: Basic task creation and display functionality

1. Create project structure (src/, models/, services/, cli/)
2. Implement Task dataclass in src/models/task.py
3. Implement TaskService with add_task() and list_tasks() in src/services/task_service.py
4. Implement basic menu in src/cli/menu.py
5. Create main.py entry point

### Phase 2: Analysis (Update + Delete + Validation)

**Goal**: Task modification and input validation

1. Add update_task() method to TaskService
2. Add delete_task() method to TaskService
3. Add input validation (non-empty title, existing ID check)
4. Update menu with Update and Delete options
5. Add error handling for invalid operations

### Phase 3: Synthesis (Toggle Complete + Integration)

**Goal**: Complete feature set with full integration

1. Add toggle_complete() method to TaskService
2. Add Toggle Complete menu option
3. Integrate colorama for colored output (✔ / ✖)
4. End-to-end testing of all features
5. Final validation against success criteria

## Testing Strategy

### Validation Checks

| Feature | Check |
|---------|-------|
| Add Task | Task appears in list with correct ID, title, description, completed=False |
| View Tasks | All tasks display with ID, title, status symbols |
| Update Task | Task details change on valid ID; error on invalid ID |
| Delete Task | Task removed; error on invalid ID |
| Toggle Complete | Status changes and symbols update; error on invalid ID |
| Menu Input | Valid options only; invalid input reprompts |

### End-to-End Checks

- Run through all 5 features sequentially
- Verify app runs in terminal without errors
- Confirm colored output displays correctly

## Quality Gates

Before marking each phase complete:

1. ✅ Code follows clean code principles (Clarity)
2. ✅ No unused code or features (Rigor)
3. ✅ All operations work as specified (Accuracy)
4. ✅ User input is validated (Reproducibility)
5. ✅ Terminal output is clear and colored (Clarity)
