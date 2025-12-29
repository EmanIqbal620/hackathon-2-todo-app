# Tasks: Advanced CLI TODO App - Intelligent Features

**Input**: Design documents from `/specs/003-todo-intelligent/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

**Tests**: Tests are NOT explicitly requested in the specification. Manual validation checklist is provided in plan.md.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root (per plan.md)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Model layer extensions needed by ALL user stories

- [x] T001 [P] Add RECURRENCE_PATTERNS constant to src/models/task.py
- [x] T002 [P] Add REMINDER_OFFSETS constant to src/models/task.py
- [x] T003 Add recurrence_pattern field to Task dataclass in src/models/task.py
- [x] T004 Add reminder_offset field to Task dataclass in src/models/task.py
- [x] T005 Add reminder_shown field to Task dataclass in src/models/task.py

**Checkpoint**: Task model now supports all new fields for intelligent features

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core service infrastructure that MUST be complete before ANY user story can be implemented

**Critical**: These tasks provide the date validation and overdue detection that US1-US4 all depend on

- [x] T006 Add _validate_date_format() helper function to src/services/task_service.py
- [x] T007 Add is_overdue() method to TaskService in src/services/task_service.py
- [x] T008 Extend add_task() to accept recurrence_pattern and reminder_offset parameters in src/services/task_service.py
- [x] T009 Extend update_task() to accept due_date, recurrence_pattern, and reminder_offset parameters in src/services/task_service.py

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Due Dates with Overdue Highlighting (Priority: P1)

**Goal**: Users can set due dates and see color-coded overdue status at a glance

**Independent Test**: Create tasks with past/present/future due dates; verify CLI table shows red (⚠ Overdue), yellow (○ Pending), or green (✓ Completed) status indicators

### Implementation for User Story 1

- [x] T010 [US1] Update COLORS dict to change 'pending' color to yellow (Fore.YELLOW) in src/cli/menu.py
- [x] T011 [US1] Add 'overdue' color entry using Fore.RED in COLORS dict in src/cli/menu.py
- [x] T012 [US1] Update column widths for new table layout (id_w=4, title_w=14, desc_w=12, due_w=10, recur_w=8, status_w=12) in src/cli/menu.py
- [x] T013 [US1] Update _display_tasks_table() header row to include Due and Recurrence columns in src/cli/menu.py
- [x] T014 [US1] Update _display_tasks_table() separator row for 6 columns in src/cli/menu.py
- [x] T015 [US1] Update _display_tasks_table() task rows to include due_date and recurrence_pattern columns in src/cli/menu.py
- [x] T016 [US1] Update _display_tasks_table() status rendering to show ⚠ Overdue (red) when is_overdue() returns True in src/cli/menu.py
- [x] T017 [US1] Update _display_task_list() to match new 6-column layout in src/cli/menu.py
- [x] T018 [US1] Verify date validation rejects invalid formats in _handle_add_task() in src/cli/menu.py

**Checkpoint**: User Story 1 complete - due dates visible with color-coded overdue highlighting

---

## Phase 4: User Story 2 - Recurring Tasks (Priority: P2)

**Goal**: Users can create recurring tasks that auto-reschedule when completed

**Independent Test**: Create a daily/weekly/monthly recurring task, mark complete, verify new task instance created with next due date

### Implementation for User Story 2

- [x] T019 [US2] Add _calculate_next_due_date() helper function to src/services/task_service.py
- [x] T020 [US2] Add _add_months() helper for monthly recurrence calculation in src/services/task_service.py
- [x] T021 [US2] Extend toggle_complete() to auto-create next instance when completing a recurring task in src/services/task_service.py
- [x] T022 [US2] Update _handle_add_task() to prompt for recurrence pattern in src/cli/menu.py
- [x] T023 [US2] Add _show_options() call for RECURRENCE_PATTERNS in _handle_add_task() in src/cli/menu.py
- [x] T024 [US2] Update _handle_update_task() to allow changing recurrence pattern in src/cli/menu.py
- [x] T025 [US2] Update _handle_toggle_complete() to display info about newly created recurring instance in src/cli/menu.py

**Checkpoint**: User Story 2 complete - recurring tasks auto-reschedule on completion

---

## Phase 5: User Story 3 - Reminder Notifications (Priority: P3)

**Goal**: Users can set reminders that display notifications when the CLI is running

**Independent Test**: Create task with reminder offset, verify notification displays when reminder time is reached

### Implementation for User Story 3

- [x] T026 [P] [US3] Create src/services/reminder_service.py with ReminderService class skeleton
- [x] T027 [US3] Implement check_due_reminders() method in ReminderService in src/services/reminder_service.py
- [x] T028 [US3] Implement _is_reminder_due() helper method in ReminderService in src/services/reminder_service.py
- [x] T029 [US3] Implement mark_reminder_shown() method in ReminderService in src/services/reminder_service.py
- [x] T030 [US3] Implement format_reminder() method in ReminderService in src/services/reminder_service.py
- [x] T031 [US3] Add _print_reminder() method to Menu class in src/cli/menu.py
- [x] T032 [US3] Integrate ReminderService into run() loop to check and display reminders in src/cli/menu.py
- [x] T033 [US3] Update _handle_add_task() to prompt for reminder offset when due date is set in src/cli/menu.py
- [x] T034 [US3] Add _show_options() call for REMINDER_OFFSETS in _handle_add_task() in src/cli/menu.py
- [x] T035 [US3] Update _handle_update_task() to allow changing reminder offset in src/cli/menu.py

**Checkpoint**: User Story 3 complete - reminders display when due

---

## Phase 6: User Story 4 - Filter/Sort/Search Extensions (Priority: P4)

**Goal**: Users can filter, sort, and search by due date and recurrence pattern

**Independent Test**: Create tasks with various due dates and recurrence patterns; verify filter/sort/search operations work correctly

### Implementation for User Story 4

- [x] T036 [US4] Extend filter_tasks() to add recurrence parameter in src/services/task_service.py
- [x] T037 [US4] Extend filter_tasks() to add overdue parameter in src/services/task_service.py
- [x] T038 [US4] Extend sort_tasks() to add 'due' sort option in src/services/task_service.py
- [x] T039 [US4] Extend search_tasks() to include recurrence_pattern in search scope in src/services/task_service.py
- [x] T040 [US4] Update _handle_filter_tasks() to add recurrence filter option in src/cli/menu.py
- [x] T041 [US4] Update _handle_filter_tasks() to add overdue filter option in src/cli/menu.py
- [x] T042 [US4] Update _handle_sort_tasks() to add 'due' sort option in src/cli/menu.py

**Checkpoint**: User Story 4 complete - all filter/sort/search extensions working

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Final validation and cleanup

- [x] T043 Verify all 6 columns display correctly in CLI table (manual test)
- [x] T044 Verify color-coded status shows green/yellow/red appropriately (manual test)
- [x] T045 Verify monthly recurrence handles month-end edge case (31st → 28th/30th) (manual test)
- [x] T046 Verify cross-platform terminal colors work (Windows, Linux, macOS) (manual test)
- [x] T047 Code cleanup and remove any duplicate update_task() method in src/services/task_service.py

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion
  - US1 (P1): Can start after Phase 2
  - US2 (P2): Can start after Phase 2 (independent of US1)
  - US3 (P3): Can start after Phase 2 (independent of US1, US2)
  - US4 (P4): Can start after Phase 2 (independent of US1, US2, US3)
- **Polish (Phase 7)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Depends on Phase 2 only - No dependencies on other stories
- **User Story 2 (P2)**: Depends on Phase 2 only - Independently testable
- **User Story 3 (P3)**: Depends on Phase 2 only - Independently testable
- **User Story 4 (P4)**: Depends on Phase 2 only - Independently testable

### Within Each Phase

- Setup: T001, T002 can run in parallel; T003, T004, T005 must follow
- Foundational: T006, T007 can run in parallel; T008, T009 depend on T006
- US1: T010, T011, T012 can run in parallel; table tasks are sequential
- US2: T019, T020 before T021; CLI tasks can follow service tasks
- US3: T026 first, then T027-T030 sequentially, then CLI tasks
- US4: T036-T039 can run in parallel; CLI tasks depend on service tasks

### Parallel Opportunities

Within each user story phase, tasks marked [P] can run in parallel. Additionally:

- **Phase 1**: T001 and T002 can run in parallel (different constants)
- **Phase 2**: T006 and T007 can run in parallel (different functions)
- **Phase 5**: T026 (create file) can run in parallel with other phases

---

## Parallel Example: User Story 1

```bash
# Launch color setup tasks together:
Task: "Update COLORS dict to change 'pending' color to yellow in src/cli/menu.py"
Task: "Add 'overdue' color entry using Fore.RED in src/cli/menu.py"
Task: "Update column widths for new table layout in src/cli/menu.py"

# Then sequential table updates:
Task: "Update _display_tasks_table() header row..."
Task: "Update _display_tasks_table() separator row..."
Task: "Update _display_tasks_table() task rows..."
Task: "Update _display_tasks_table() status rendering..."
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (Task model extensions)
2. Complete Phase 2: Foundational (date validation, overdue detection)
3. Complete Phase 3: User Story 1 (due dates with overdue highlighting)
4. **STOP and VALIDATE**: Test color-coded status indicators
5. Deploy/demo if ready

### Incremental Delivery

1. Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → **MVP Complete!**
3. Add User Story 2 → Test recurring tasks → Deploy/Demo
4. Add User Story 3 → Test reminders → Deploy/Demo
5. Add User Story 4 → Test filter/sort/search → Deploy/Demo
6. Each story adds value without breaking previous stories

### Sequential Delivery (Recommended)

Given single-developer scenario and file overlap in CLI:

1. Phase 1 → Phase 2 → Phase 3 (US1) → Phase 4 (US2) → Phase 5 (US3) → Phase 6 (US4) → Phase 7

---

## Summary

| Phase | Task Count | Key Deliverable |
|-------|------------|-----------------|
| Setup | 5 | Task model with new fields |
| Foundational | 4 | Date validation + overdue detection |
| US1 (P1) | 9 | Due dates + color-coded status |
| US2 (P2) | 7 | Recurring tasks + auto-reschedule |
| US3 (P3) | 10 | Reminder service + notifications |
| US4 (P4) | 7 | Filter/sort/search extensions |
| Polish | 5 | Manual validation |
| **Total** | **47** | Full intelligent features |

---

## Notes

- [P] tasks = different files or independent functions, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story is independently completable and testable after Phase 2
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- src/cli/menu.py has most changes - avoid parallel edits to same file
