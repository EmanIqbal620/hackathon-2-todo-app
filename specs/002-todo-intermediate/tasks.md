# Tasks: Intermediate Level Todo CLI – Hackathon 2 Phase I

**Input**: Design documents from `/specs/002-todo-intermediate/`
**Prerequisites**: plan.md (complete), spec.md (complete)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project structure per plan.md

---

## Phase 1: Foundation (Data Model Enhancement)

**Purpose**: Update Task model with priority and category fields (blocking prerequisite for all user stories)

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T001 Update Task dataclass in src/models/task.py to add priority field (High/Medium/Low, default Medium)
- [x] T002 Update Task dataclass in src/models/task.py to add category field (Work/Home/Personal, default Personal)
- [x] T003 [P] Add updated_flag field to Task dataclass in src/models/task.py
- [x] T004 Update TaskService.add_task() in src/services/task_service.py to accept priority and category parameters
- [x] T005 Update TaskService.get_task() in src/services/task_service.py to handle updated_flag if needed

**Checkpoint**: Foundation ready - all user stories can now be implemented

---

## Phase 2: User Story 1 - Add Task with Priority and Category (Priority: P1) 🎯 MVP

**Goal**: Users can create tasks with priority levels and categories

**Independent Test**: Add a task with priority/category and verify they appear correctly in the task list

- [x] T006 [P] [US1] Update _handle_add_task() in src/cli/menu.py to prompt for priority (High/Medium/Low)
- [x] T007 [P] [US1] Update _handle_add_task() in src/cli/menu.py to prompt for category (Work/Home/Personal)
- [x] T008 [US1] Verify TaskService.add_task() passes priority and category to new Task creation

**Checkpoint**: User Story 1 complete - tasks can be created with priority and category

---

## Phase 3: User Story 5 - View Enhanced Task Table (Priority: P1) 🎯 MVP

**Goal**: Display tasks with priority and category in polished table format

**Independent Test**: Add tasks with different attributes and verify the table displays all columns

- [x] T009 [P] [US5] Update _display_tasks_list() in src/cli/menu.py to show 6 columns: ID, User ID, Title, Priority, Category, Status
- [x] T010 [P] [US5] Add color coding for priority in src/cli/menu.py (High=Red, Medium=Yellow, Low=Green)
- [x] T011 [US5] Format task display to show priority and category values correctly

**Checkpoint**: User Story 5 complete - enhanced table displays all task information

---

## Phase 4: User Story 2 - Search Tasks (Priority: P1) 🎯 MVP

**Goal**: Users can search tasks by keyword in title and description

**Independent Test**: Add multiple tasks with different titles and verify search returns correct results

- [x] T012 [P] [US2] Implement search_tasks() method in src/services/task_service.py for keyword search
- [x] T013 [P] [US2] Make search case-insensitive in search_tasks() method
- [x] T014 [US2] Add search_tasks() to match title OR description
- [x] T015 [US2] Add Search Tasks menu option in src/cli/menu.py
- [x] T016 [US2] Implement _handle_search_tasks() in src/cli/menu.py to prompt for keyword and display results

**Checkpoint**: User Story 2 complete - users can search tasks by keyword

---

## Phase 5: User Story 3 - Filter Tasks (Priority: P2)

**Goal**: Users can filter tasks by status, priority, or category

**Independent Test**: Create tasks with different attributes and verify filters return only matching tasks

- [x] T017 [P] [US3] Implement filter_tasks() method in src/services/task_service.py for status filtering
- [x] T018 [P] [US3] Extend filter_tasks() in src/services/task_service.py for priority filtering
- [x] T019 [P] [US3] Extend filter_tasks() in src/services/task_service.py for category filtering
- [x] T020 [P] [US3] Support combinable filters (AND logic) in filter_tasks() method
- [x] T021 [US3] Add Filter Tasks menu option in src/cli/menu.py
- [x] T022 [US3] Implement _handle_filter_tasks() in src/cli/menu.py to prompt for filter criteria and display results

**Checkpoint**: User Story 3 complete - users can filter tasks by multiple criteria

---

## Phase 6: User Story 4 - Sort Tasks (Priority: P2)

**Goal**: Users can sort tasks by priority, alphabetically, or by date

**Independent Test**: Create tasks with different priorities and verify sort order

- [x] T023 [P] [US4] Implement sort_tasks() method in src/services/task_service.py for priority sorting (High → Medium → Low)
- [x] T024 [P] [US4] Extend sort_tasks() in src/services/task_service.py for alphabetical sorting (A → Z)
- [x] T025 [P] [US4] Extend sort_tasks() in src/services/task_service.py for date sorting (newest first)
- [x] T026 [US4] Add Sort Tasks menu option in src/cli/menu.py
- [x] T027 [US4] Implement _handle_sort_tasks() in src/cli/menu.py to prompt for sort criteria and display results

**Checkpoint**: User Story 4 complete - users can sort tasks by various criteria

---

## Phase 7: User Story 6 - Update Task with Priority and Category (Priority: P2)

**Goal**: Users can modify priority and category of existing tasks

**Independent Test**: Update a task's priority/category and verify the changes

- [x] T028 [US6] Update _handle_update_task() in src/cli/menu.py to allow changing priority
- [x] T029 [US6] Update _handle_update_task() in src/cli/menu.py to allow changing category
- [x] T030 [US6] Verify updated priority and category appear in enhanced table view

**Checkpoint**: User Story 6 complete - users can update priority and category

---

## Phase 8: Integration & Cross-Cutting Concerns

**Purpose**: Connect all features and ensure Phase I compatibility

- [x] T031 Connect Add Task priority/category input to TaskService.add_task()
- [x] T032 Connect Update Task priority/category modification to TaskService.update_task()
- [x] T033 Ensure all Phase I features (Add, Update, Delete, Toggle Complete, View) still work
- [x] T034 Verify search, filter, and sort work together (filtered results can be sorted)
- [x] T035 Add Filter menu option to main menu (expand from 6 to 9 options)
- [x] T036 Add Search menu option to main menu
- [x] T037 Add Sort menu option to main menu
- [x] T038 Run end-to-end testing: Add → Search → Filter → Sort → Update → View
- [x] T039 Verify terminal UI maintains polished appearance with boxes, colors, and consistent formatting
- [x] T040 Verify exit message displays "Allah Hafiz" as in Phase I

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Foundation)**: No dependencies - start here (BLOCKS all user stories)
- **Phase 2 (US1 Add Priority/Category)**: Depends on Phase 1
- **Phase 3 (US5 Enhanced Table)**: Depends on Phase 1
- **Phase 4 (US2 Search)**: Depends on Phase 1
- **Phase 5 (US3 Filter)**: Depends on Phase 1
- **Phase 6 (US4 Sort)**: Depends on Phase 1
- **Phase 7 (US6 Update P/C)**: Depends on Phase 1
- **Phase 8 (Integration)**: Depends on all user story phases

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Phase 1 - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Phase 1 - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Phase 1 - No dependencies on other stories
- **User Story 4 (P2)**: Can start after Phase 1 - No dependencies on other stories
- **User Story 5 (P1)**: Can start after Phase 1 - No dependencies on other stories
- **User Story 6 (P2)**: Can start after Phase 1 - No dependencies on other stories

### Within Each User Story

- Tasks marked [P] can run in parallel within the story
- Menu integration depends on service methods being complete

### Parallel Opportunities

- T001, T002, T003: Different fields, can run in parallel
- T006, T007: Different menu prompts, can run in parallel
- T009, T010: Different UI features, can run in parallel
- T012, T013: Different search features, can run in parallel
- T017, T018, T019: Different filter types, can run in parallel
- T023, T024, T025: Different sort types, can run in parallel

---

## Implementation Strategy

### MVP First (User Story 1 + User Story 5)

1. Complete Phase 1: Foundation
2. Complete Phase 2: User Story 1 (Add with Priority/Category)
3. Complete Phase 3: User Story 5 (Enhanced Table)
4. **STOP and VALIDATE**: Test Add Task with priority/category displays correctly
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Phase 1 → Foundation ready
2. Add User Story 1 → Test independently → MVP (Add + View with Priority/Category)
3. Add User Story 2 → Test independently → Search functionality
4. Add User Story 3 → Test independently → Filter functionality
5. Add User Story 4 → Test independently → Sort functionality
6. Add User Story 5 → Enhanced table display
7. Add User Story 6 → Update Priority/Category
8. Complete Phase 8 → Full Phase II feature set

### Parallel Team Strategy

With multiple developers:

1. Team completes Phase 1 together
2. Once Phase 1 is done:
   - Developer A: User Story 1 (Add Priority/Category)
   - Developer B: User Story 5 (Enhanced Table)
   - Developer C: User Story 2 (Search)
3. Continue with remaining user stories in parallel

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each phase completion
- Stop at checkpoints to validate story independently
- All file paths are relative to repository root
