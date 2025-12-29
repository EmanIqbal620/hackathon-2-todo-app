# Implementation Plan: Advanced CLI TODO App - Intelligent Features

**Branch**: `003-todo-intelligent` | **Date**: 2025-12-28 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/003-todo-intelligent/spec.md`

## Summary

Extend the existing Todo CLI application with intelligent task management features: recurring tasks with auto-rescheduling, enhanced due date tracking with overdue highlighting, optional reminder notifications, and extended filter/sort/search capabilities. The implementation preserves the existing professional CLI table layout while adding "Due" and "Recurrence" columns with color-coded status indicators.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: colorama (already in use), datetime (stdlib)
**Storage**: In-memory only (list of Task objects)
**Testing**: pytest (unit tests), manual CLI testing
**Target Platform**: Windows, Linux, macOS (cross-platform CLI)
**Project Type**: Single CLI application
**Performance Goals**: All operations < 2 seconds with up to 100 tasks
**Constraints**: No database, no external APIs, no GUI, no OS-level notifications
**Scale/Scope**: Single-user CLI application, in-memory storage

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Accuracy | PASS | All new features will work exactly as specified in FR-001 through FR-023 |
| II. Clarity | PASS | New code follows existing patterns with clear function/variable names |
| III. Reproducibility | PASS | Task operations remain consistent; recurring task creation is deterministic |
| IV. Rigor | PASS | Features strictly follow spec; no scope creep beyond defined requirements |
| V. Simplicity | PASS | Minimal changes to existing architecture; no over-engineering |

**Constitution Amendments Required**: The constitution lists "Due dates", "Categories", and "Priorities" as prohibited features. However, the existing codebase already implements these (see `src/models/task.py:19-29`). This plan assumes the constitution has been superseded by the feature evolution tracked in branch `002-todo-intermediate`. The `003-todo-intelligent` feature builds on that foundation.

## Project Structure

### Documentation (this feature)

```text
specs/003-todo-intelligent/
├── spec.md              # Feature specification
├── plan.md              # This file
├── checklists/
│   └── requirements.md  # Spec quality checklist
└── tasks.md             # Will be created by /sp.tasks
```

### Source Code (repository root)

```text
src/
├── __init__.py
├── main.py              # Entry point (no changes needed)
├── models/
│   ├── __init__.py
│   └── task.py          # MODIFY: Add recurrence_pattern, reminder_offset, reminder_shown
├── services/
│   ├── __init__.py
│   ├── task_service.py  # MODIFY: Add recurrence engine, overdue detection
│   └── reminder_service.py  # NEW: Reminder checking and notification
└── cli/
    ├── __init__.py
    └── menu.py          # MODIFY: Update table display, add Due/Recurrence columns

tests/
├── __init__.py
├── unit/
│   ├── __init__.py
│   ├── test_task_model.py
│   ├── test_task_service.py
│   └── test_reminder_service.py
└── integration/
    ├── __init__.py
    └── test_cli_flow.py
```

**Structure Decision**: Single project structure maintained. New `reminder_service.py` added to services layer for separation of concerns. Tests organized into unit and integration subdirectories.

## Complexity Tracking

No constitution violations requiring justification. All changes follow the Simplicity principle.

---

## Architecture Overview

### Module Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                           CLI Layer                             │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                     menu.py                              │   │
│  │  - Display tasks table (+ Due, Recurrence columns)      │   │
│  │  - Color-coded status (✓ green, ○ yellow, ⚠ red)        │   │
│  │  - Handle add/update with recurrence & reminder input   │   │
│  │  - Show reminder notifications                           │   │
│  └─────────────────────────────────────────────────────────┘   │
└──────────────────────────────┬──────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│                        Service Layer                            │
│  ┌────────────────────────┐    ┌────────────────────────────┐  │
│  │    task_service.py     │    │   reminder_service.py      │  │
│  │  - CRUD operations     │    │  - Check due reminders     │  │
│  │  - Toggle complete     │    │  - Calculate reminder time │  │
│  │  - Auto-reschedule     │    │  - Track shown reminders   │  │
│  │  - Overdue detection   │    │  - Format notification     │  │
│  │  - Filter/Sort/Search  │    └────────────────────────────┘  │
│  └────────────────────────┘                                     │
└──────────────────────────────┬──────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│                         Model Layer                             │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                      task.py                             │   │
│  │  @dataclass Task:                                        │   │
│  │    id, user_id, title, description, completed,           │   │
│  │    priority, category, due_date, updated_flag,           │   │
│  │    recurrence_pattern, reminder_offset, reminder_shown   │   │
│  │                                                          │   │
│  │  RECURRENCE_PATTERNS = ["None", "Daily", "Weekly", "Monthly"] │
│  │  REMINDER_OFFSETS = ["None", "1 day", "1 hour", "At due"] │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Section 1: Task CRUD Extensions

### 1.1 Model Changes (`src/models/task.py`)

**Current State**: Task dataclass with id, user_id, title, description, completed, priority, category, due_date, updated_flag.

**Changes Required**:

```python
# Add new fields to Task dataclass
recurrence_pattern: str = "None"  # None | Daily | Weekly | Monthly
reminder_offset: str = "None"     # None | 1 day | 1 hour | At due
reminder_shown: bool = False      # Track if reminder was displayed

# Add new constants
RECURRENCE_PATTERNS = ["None", "Daily", "Weekly", "Monthly"]
REMINDER_OFFSETS = ["None", "1 day", "1 hour", "At due"]
```

**Design Decision**: Use strings for recurrence_pattern and reminder_offset instead of Enum for simplicity and direct comparison with user input. This follows the existing pattern for priority and category.

### 1.2 Service Changes (`src/services/task_service.py`)

**Extend `add_task()`**:
- Add parameters: `recurrence_pattern="None"`, `reminder_offset="None"`
- Validate recurrence_pattern and reminder_offset against allowed values

**Extend `update_task()`**:
- Add parameters: `recurrence_pattern`, `reminder_offset`, `due_date`
- Allow updating these new fields

**Keep existing methods unchanged**: `list_tasks()`, `get_task()`, `delete_task()` work without modification.

---

## Section 2: Recurrence Engine

### 2.1 Auto-Rescheduling Logic

**Location**: `src/services/task_service.py` - extend `toggle_complete()` method

**Algorithm**:

```
When toggle_complete(task_id) is called AND task.completed becomes True:
  IF task.recurrence_pattern != "None":
    1. Calculate next_due_date based on pattern:
       - Daily: current_due_date + 1 day
       - Weekly: current_due_date + 7 days
       - Monthly: current_due_date + 1 month (handle month-end edge cases)
    2. Create new task with:
       - Same: title, description, priority, category, recurrence_pattern, reminder_offset
       - New: id (auto-increment), due_date = next_due_date
       - Reset: completed = False, reminder_shown = False
    3. Return both original task (now completed) and new task
```

**Month-End Edge Case**: When adding 1 month to Jan 31, result should be Feb 28 (or 29 in leap year). Use Python's `calendar.monthrange()` or `dateutil.relativedelta` (stdlib preferred to avoid new dependency).

**Implementation Approach**: Use `datetime` stdlib module with manual month arithmetic to avoid adding dependencies.

### 2.2 Date Calculation Helper

**New function** in `task_service.py`:

```python
def _calculate_next_due_date(current_due: str, pattern: str) -> str:
    """Calculate next due date based on recurrence pattern.

    Args:
        current_due: Current due date in YYYY-MM-DD format
        pattern: Recurrence pattern (Daily/Weekly/Monthly)

    Returns:
        Next due date in YYYY-MM-DD format
    """
```

---

## Section 3: Due Dates & Reminders

### 3.1 Overdue Detection

**Location**: `src/services/task_service.py`

**New method**:

```python
def is_overdue(self, task: Task) -> bool:
    """Check if a task is overdue.

    Returns True if:
    - task has a due_date
    - task is not completed
    - due_date < today's date
    """
```

**Usage**: Called by CLI layer when rendering task status.

### 3.2 Reminder Service (`src/services/reminder_service.py`)

**New module** - keeps reminder logic separate from task CRUD.

```python
class ReminderService:
    """Handles reminder checking and notifications."""

    def check_due_reminders(self, tasks: List[Task]) -> List[Task]:
        """Return tasks that need reminder notification now."""

    def _is_reminder_due(self, task: Task) -> bool:
        """Check if task's reminder time has been reached."""

    def mark_reminder_shown(self, task: Task) -> None:
        """Mark task's reminder as shown to prevent duplicates."""

    def format_reminder(self, task: Task) -> str:
        """Format reminder message for CLI display."""
```

**Reminder Calculation**:
- "1 day": due_date - 24 hours
- "1 hour": due_date - 1 hour (requires time component, default to 00:00)
- "At due": due_date at 00:00

**Note**: Since we only store dates (not times), "1 hour" and "At due" will effectively trigger on the due date. This is acceptable per spec (CLI-based, in-memory only).

### 3.3 Date Validation

**Location**: `src/services/task_service.py`

**New helper function**:

```python
def _validate_date_format(date_str: str) -> bool:
    """Validate date string is in YYYY-MM-DD format and is a valid date."""
```

**Usage**: Called when adding/updating tasks with due dates.

---

## Section 4: Search, Filter, Sort Extensions

### 4.1 Extended Filter (`src/services/task_service.py`)

**Modify `filter_tasks()`** to add:

```python
def filter_tasks(
    self,
    status: str = "All",      # Existing: All/Pending/Completed
    priority: str = "All",    # Existing
    category: str = "All",    # Existing
    recurrence: str = "All",  # NEW: All/None/Daily/Weekly/Monthly
    overdue: bool = False     # NEW: True = only overdue tasks
) -> List[Task]:
```

**Overdue filter logic**: When `overdue=True`, filter to tasks where `is_overdue(task)` returns True.

### 4.2 Extended Sort (`src/services/task_service.py`)

**Modify `sort_tasks()`** to add due_date option:

```python
def sort_tasks(
    self,
    tasks: List[Task],
    sort_by: str = "date",  # Existing: date/priority/alpha, NEW: due
    direction: str = "desc"
) -> List[Task]:
```

**Due date sorting**:
- Tasks with due dates sort by due_date
- Tasks without due dates sort to the end (ascending) or beginning (descending)

### 4.3 Extended Search (`src/services/task_service.py`)

**Modify `search_tasks()`** to include recurrence pattern in search scope:

```python
def search_tasks(self, keyword: str) -> List[Task]:
    """Search tasks by keyword in title, description, and recurrence pattern."""
```

---

## Section 5: CLI Table Display

### 5.1 Table Layout Update (`src/cli/menu.py`)

**Current columns**: ID | Title | Description | Status

**New columns**: ID | Title | Description | Due | Recurrence | Status

**Column widths** (adjusted for new columns within WIDTH=62):

```python
id_w = 4       # Was 5
title_w = 14   # Was 18
desc_w = 12    # Was 18
due_w = 10     # NEW: YYYY-MM-DD
recur_w = 8    # NEW: Daily/Weekly/Monthly/—
status_w = 12  # Was 14
# Total: 4 + 14 + 12 + 10 + 8 + 12 = 60 (+ 2 for spacing = 62)
```

### 5.2 Color-Coded Status Indicators

**Status rendering logic**:

```python
if task.completed:
    status = f"{GREEN}✓ Completed{RESET}"
elif is_overdue(task):
    status = f"{RED}⚠ Overdue{RESET}"
else:
    status = f"{YELLOW}○ Pending{RESET}"
```

**Color mapping** (using existing COLORS dict):
- Completed: `COLORS['completed']` (green) - already exists
- Pending: `COLORS['pending']` - change to yellow
- Overdue: `COLORS['error']` (red) - reuse existing

### 5.3 Reminder Notification Display

**Location**: `menu.py` - at the start of each main loop iteration

**Logic**:
```python
# In run() method, before displaying tasks:
reminder_service = ReminderService()
due_reminders = reminder_service.check_due_reminders(self.task_service.list_tasks())
for task in due_reminders:
    self._print_reminder(task)
    reminder_service.mark_reminder_shown(task)
```

**New method**:
```python
def _print_reminder(self, task: Task) -> None:
    """Print a reminder notification for a task."""
    # Use existing notification style with bell icon 🔔
```

### 5.4 Menu Updates

**Add Task flow** - add prompts for:
1. Recurrence pattern (optional, default: None)
2. Reminder offset (optional, default: None) - only if due date is set

**Update Task flow** - add prompts for:
1. New due date (optional)
2. New recurrence pattern (optional)
3. New reminder offset (optional)

**Filter Tasks flow** - add options for:
1. Recurrence filter: All | None | Daily | Weekly | Monthly
2. Overdue filter: All | Overdue only

**Sort Tasks flow** - add option:
1. Sort by: date | priority | alpha | **due**

---

## Architectural Decisions

### ADR-001: In-Memory Storage (Confirmed)

**Decision**: Continue using in-memory storage (Python list) for tasks.

**Context**: Spec explicitly states "In-memory task storage only" and "Database persistence" is out of scope.

**Consequences**:
- Tasks are lost on application exit (acceptable per spec)
- No need for JSON backup implementation
- Simplest possible storage solution

### ADR-002: Manual Date Calculation

**Decision**: Use Python stdlib `datetime` for date calculations without external libraries.

**Context**: Need to calculate next due dates for recurring tasks. Options considered:
1. `datetime` stdlib - no new dependencies, handles basic date math
2. `dateutil.relativedelta` - better month handling but adds dependency
3. `arrow` or `pendulum` - feature-rich but unnecessary complexity

**Chosen**: Option 1 (`datetime` stdlib)

**Rationale**:
- Follows Simplicity principle
- No new dependencies to manage
- Month-end edge cases can be handled with simple calendar logic

**Implementation**:
```python
from datetime import datetime, timedelta
import calendar

def add_months(date: datetime, months: int) -> datetime:
    """Add months to date, handling month-end edge cases."""
    month = date.month + months
    year = date.year + (month - 1) // 12
    month = ((month - 1) % 12) + 1
    day = min(date.day, calendar.monthrange(year, month)[1])
    return date.replace(year=year, month=month, day=day)
```

### ADR-003: CLI-Based Reminders Only

**Decision**: Implement reminders as CLI notifications displayed when the application is running.

**Context**: Spec states "Reminders are CLI-based notifications (printed messages), not OS-level notifications."

**Consequences**:
- Reminders only work while CLI is active
- No background daemon or system tray
- Reminders checked at each main loop iteration
- Missed reminders (CLI not running) are shown on next startup if still relevant

---

## Quality Validation Plan

### Unit Tests

| Test File | Coverage |
|-----------|----------|
| `test_task_model.py` | Task dataclass with new fields, constants |
| `test_task_service.py` | CRUD with recurrence, overdue detection, date calculation, filter/sort extensions |
| `test_reminder_service.py` | Reminder checking, due calculation, shown tracking |

### Integration Tests

| Test File | Coverage |
|-----------|----------|
| `test_cli_flow.py` | End-to-end flows: add recurring task → complete → verify new instance |

### Manual Validation

- [ ] CLI table displays all 6 columns correctly
- [ ] Color-coded status shows green/yellow/red appropriately
- [ ] Recurring task creates new instance on completion
- [ ] Daily/Weekly/Monthly recurrence calculates correct next date
- [ ] Monthly recurrence handles month-end edge case (31st → 28th/30th)
- [ ] Overdue tasks show red warning indicator
- [ ] Filter by recurrence pattern works
- [ ] Sort by due date works (nulls at end)
- [ ] Search includes recurrence pattern
- [ ] Reminders display when due
- [ ] Cross-platform: Windows, Linux, macOS terminal colors

---

## Risk Analysis

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Month-end date calculation bugs | Medium | Medium | Comprehensive unit tests for edge cases |
| Table column width overflow | Low | Low | Test with long titles; truncation already implemented |
| Colorama compatibility issues | Low | Medium | Already in use; test on all platforms |
| Performance with 100+ tasks | Low | Low | All operations are O(n) which is acceptable |

---

## Implementation Order

1. **Phase 1**: Model changes (Task dataclass extensions)
2. **Phase 2**: Task service extensions (date validation, overdue detection)
3. **Phase 3**: Recurrence engine (auto-rescheduling on completion)
4. **Phase 4**: Reminder service (new module)
5. **Phase 5**: CLI updates (table layout, color-coded status)
6. **Phase 6**: Filter/Sort/Search extensions
7. **Phase 7**: Integration testing and validation

---

## Next Steps

Run `/sp.tasks` to generate the detailed task breakdown for implementation.
