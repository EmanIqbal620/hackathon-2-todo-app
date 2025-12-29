# Feature Specification: Advanced CLI TODO App - Intelligent Features

**Feature Branch**: `003-todo-intelligent`
**Created**: 2025-12-28
**Status**: Draft
**Input**: User description: "Advanced CLI TODO App - Intelligent Features: Recurring tasks, due dates, reminders, auto-rescheduling, overdue highlighting"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Manage Due Dates with Overdue Highlighting (Priority: P1)

As a CLI user, I want to set due dates for my tasks and see at a glance which tasks are overdue, so that I can prioritize urgent work and never miss deadlines.

**Why this priority**: Due date tracking and overdue highlighting form the foundation for time-sensitive task management. Without this, recurring tasks and reminders have no temporal anchor.

**Independent Test**: Can be fully tested by creating tasks with past, present, and future due dates and verifying the CLI table displays appropriate color-coded status indicators.

**Acceptance Scenarios**:

1. **Given** a user is adding a new task, **When** they enter a due date in YYYY-MM-DD format, **Then** the task is saved with that due date and displays in the "Due" column.
2. **Given** a task has a due date in the past and is not completed, **When** the task list is displayed, **Then** that task shows a red overdue indicator (⚠).
3. **Given** a task has a due date today or in the future and is pending, **When** the task list is displayed, **Then** that task shows a yellow pending indicator (○).
4. **Given** a task is marked as completed, **When** the task list is displayed, **Then** that task shows a green completed indicator (✓) regardless of due date.
5. **Given** a user views tasks, **When** any task is overdue, **Then** the status column clearly distinguishes overdue from regular pending status.

---

### User Story 2 - Create and Manage Recurring Tasks (Priority: P2)

As a CLI user, I want to set tasks to recur on a schedule (daily, weekly, monthly), so that routine tasks automatically reappear without manual re-entry.

**Why this priority**: Recurring tasks build on the due date foundation and significantly reduce manual task entry for routine activities.

**Independent Test**: Can be fully tested by creating a recurring task, marking it complete, and verifying a new instance is automatically created with the next due date.

**Acceptance Scenarios**:

1. **Given** a user is adding a new task, **When** they select a recurrence pattern (daily/weekly/monthly), **Then** the task is saved with that recurrence pattern and displays in the "Recurrence" column.
2. **Given** a daily recurring task with due date 2025-01-01 is marked complete, **When** the completion is processed, **Then** a new task with the same details is created with due date 2025-01-02.
3. **Given** a weekly recurring task with due date 2025-01-01 is marked complete, **When** the completion is processed, **Then** a new task with the same details is created with due date 2025-01-08.
4. **Given** a monthly recurring task with due date 2025-01-15 is marked complete, **When** the completion is processed, **Then** a new task with the same details is created with due date 2025-02-15.
5. **Given** a recurring task is deleted (not completed), **When** the deletion is confirmed, **Then** no new instance is created.
6. **Given** a non-recurring task is marked complete, **When** the completion is processed, **Then** no new task is created.

---

### User Story 3 - Optional Reminder Notifications (Priority: P3)

As a CLI user, I want to receive timely reminders about upcoming due dates, so that I can prepare for tasks before they become overdue.

**Why this priority**: Reminders enhance the value of due dates but are optional - the system remains fully functional without them.

**Independent Test**: Can be fully tested by setting a reminder on a task and verifying the notification appears at the specified time when the CLI is running.

**Acceptance Scenarios**:

1. **Given** a user is adding or editing a task with a due date, **When** they set a reminder offset (e.g., 1 day before, 1 hour before), **Then** the reminder is saved with the task.
2. **Given** a task has a reminder set for "1 day before" the due date, **When** the current time reaches that threshold and the CLI is active, **Then** a notification is displayed to the user.
3. **Given** a task without a reminder set, **When** the due date approaches, **Then** no reminder notification is displayed.
4. **Given** a reminder has already been shown for a task, **When** the CLI refreshes, **Then** the same reminder is not shown again (until next occurrence for recurring tasks).

---

### User Story 4 - Filter/Sort/Search by Due Date and Recurrence (Priority: P4)

As a CLI user, I want to filter, sort, and search tasks by due date and recurrence pattern, so that I can organize and find time-sensitive tasks efficiently.

**Why this priority**: Builds on existing filter/sort/search functionality - the app already has this infrastructure, just needs extension.

**Independent Test**: Can be fully tested by creating tasks with various due dates and recurrence patterns, then verifying filter, sort, and search operations correctly include these criteria.

**Acceptance Scenarios**:

1. **Given** multiple tasks with various due dates, **When** the user sorts by due date ascending, **Then** tasks are ordered from earliest to latest due date (tasks without due dates appear at the end).
2. **Given** multiple tasks with various due dates, **When** the user sorts by due date descending, **Then** tasks are ordered from latest to earliest due date.
3. **Given** tasks with different recurrence patterns, **When** the user filters by recurrence (e.g., "Weekly"), **Then** only tasks with that recurrence pattern are displayed.
4. **Given** the user performs a search, **When** the search term matches a recurrence pattern name, **Then** tasks with that recurrence are included in results.
5. **Given** the filter options, **When** the user selects "Overdue" status filter, **Then** only overdue tasks (past due date, not completed) are shown.

---

### Edge Cases

- What happens when a monthly recurring task falls on the 31st and the next month has fewer days? (Task reschedules to the last day of the shorter month)
- What happens when a due date is entered in an invalid format? (System rejects the input and prompts for correct format)
- What happens when a recurring task is edited to remove the recurrence? (Task becomes a one-time task; no new instances created on completion)
- What happens when the system date changes while the CLI is running? (Overdue status updates on next task list refresh)
- What happens when a reminder time is set but the CLI is not running? (Reminder is shown on next CLI startup if still relevant)

## Requirements *(mandatory)*

### Functional Requirements

**Due Dates & Overdue Detection**
- **FR-001**: System MUST accept due dates in YYYY-MM-DD format when creating or editing tasks
- **FR-002**: System MUST calculate overdue status by comparing task due date to current system date
- **FR-003**: System MUST display overdue tasks with a distinct red indicator (⚠ Overdue) in the status column
- **FR-004**: System MUST display pending tasks (not overdue) with a yellow indicator (○ Pending)
- **FR-005**: System MUST display completed tasks with a green indicator (✓ Completed)
- **FR-006**: System MUST add a "Due" column to the CLI task table showing the due date

**Recurring Tasks**
- **FR-007**: System MUST support three recurrence patterns: Daily, Weekly, Monthly
- **FR-008**: System MUST add a "Recurrence" column to the CLI task table showing the pattern (or "—" for one-time tasks)
- **FR-009**: System MUST auto-create a new task instance when a recurring task is marked complete
- **FR-010**: System MUST calculate the next due date based on the recurrence pattern (daily: +1 day, weekly: +7 days, monthly: +1 month)
- **FR-011**: System MUST preserve all task properties (title, description, priority, category, recurrence) when creating the next instance
- **FR-012**: System MUST NOT create new instances when a recurring task is deleted (only on completion)

**Reminders/Notifications**
- **FR-013**: System MUST allow optional reminder settings on tasks with due dates
- **FR-014**: System MUST support reminder offsets: 1 day before, 1 hour before, at due time
- **FR-015**: System MUST display reminder notifications in the CLI when the reminder time is reached (while CLI is running)
- **FR-016**: System MUST track which reminders have been shown to avoid duplicate notifications

**Filtering, Sorting, and Searching**
- **FR-017**: System MUST extend sort options to include sorting by due date
- **FR-018**: System MUST extend filter options to include filtering by recurrence pattern
- **FR-019**: System MUST extend filter options to include an "Overdue" status filter
- **FR-020**: System MUST include recurrence pattern in search scope

**UI/Table Layout**
- **FR-021**: System MUST maintain the existing professional CLI table layout
- **FR-022**: System MUST add "Due" and "Recurrence" columns to the task table
- **FR-023**: System MUST use color-coding consistent with success criteria (green/yellow/red for status)

### Key Entities

- **Task (Extended)**: Represents a todo item. Extended attributes: due_date (optional date), recurrence_pattern (None/Daily/Weekly/Monthly), reminder_offset (None/1day/1hour/atDue), reminder_shown (boolean for tracking notification state)
- **Recurrence Pattern**: Enumeration representing repetition frequency - Daily (every 1 day), Weekly (every 7 days), Monthly (every 1 calendar month)
- **Reminder Offset**: Enumeration representing when to notify - None, 1 day before, 1 hour before, at due time

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can create a task with a due date and recurrence pattern in under 30 seconds
- **SC-002**: Overdue tasks are visually distinguishable from pending tasks within 1 second of viewing the task list
- **SC-003**: Recurring tasks automatically generate the next instance within 1 second of marking complete
- **SC-004**: 100% of overdue tasks display the red warning indicator (⚠)
- **SC-005**: Filtering by "Overdue" status returns only tasks that are past due and not completed
- **SC-006**: Sorting by due date correctly orders tasks from earliest to latest (or reverse)
- **SC-007**: CLI table displays all columns (ID, Title, Description, Due, Recurrence, Status) in a readable, professional format
- **SC-008**: Application remains responsive (all operations complete in under 2 seconds) with up to 100 tasks
- **SC-009**: Color-coded status indicators display correctly on Windows, Linux, and macOS terminals

## Assumptions

- The CLI is the primary interface; no GUI or web interface is being built
- In-memory storage is acceptable; data persistence across sessions is out of scope
- Users understand YYYY-MM-DD date format
- Reminders are CLI-based notifications (printed messages), not OS-level notifications
- The system clock is accurate and trusted for date/time calculations
- Cross-platform terminal color support via colorama library (already in use)

## Out of Scope

- GUI interface
- Database persistence
- Cloud sync
- Mobile notifications / OS-level notifications
- Natural language date parsing (e.g., "next Tuesday")
- Custom recurrence patterns beyond daily/weekly/monthly
- Snooze functionality for reminders
- Multiple reminder times per task
