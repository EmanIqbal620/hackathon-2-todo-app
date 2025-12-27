# Tasks: In-Memory Python CLI Todo Application

**Input**: Design documents from `/specs/001-todo-cli/`
**Prerequisites**: plan.md (complete), spec.md (complete)

**Organization**: Tasks are grouped by phase to enable incremental implementation.

## Format: `[ID] [P?] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project structure per plan.md

---

## Phase 1: Foundation

**Purpose**: Project initialization and core features (Add + View Tasks)

**Checkpoint**: After this phase, basic MVP should be functional

- [x] T001 [P] Create project structure per plan.md (src/, src/models/, src/services/, src/cli/)
- [x] T002 [P] Create __init__.py files for all packages
- [x] T003 Create src/main.py with basic application entry point
- [x] T004 [P] Create Task dataclass in src/models/task.py with id, title, description, completed fields
- [x] T005 [P] Create src/services/task_service.py with TaskService class and in-memory task list
- [x] T006 [P] Implement add_task() method in TaskService (validates non-empty title, auto-increment ID)
- [x] T007 [P] Implement list_tasks() method in TaskService (returns all tasks with details)
- [x] T008 Create src/cli/menu.py with basic menu interface (Add, View, Update, Delete, Toggle Complete, Exit)
- [x] T009 Connect add_task() and list_tasks() to menu options

---

## Phase 2: Analysis

**Purpose**: Update + Delete functionality and input validation

**Checkpoint**: All CRUD operations work with proper validation

- [x] T010 Implement update_task() method in TaskService (validates ID exists, updates title/description)
- [x] T011 Implement delete_task() method in TaskService (validates ID exists, removes task)
- [x] T012 Connect Update Task option in menu to update_task()
- [x] T013 Connect Delete Task option in menu to delete_task()
- [x] T014 Add input validation for menu (reject invalid options, reprompt user)
- [x] T015 Add input validation for Add Task (reject empty title)
- [x] T016 Add input validation for Update Task (reject non-existent ID)
- [x] T017 Add input validation for Delete Task (reject non-existent ID)
- [x] T018 Add user-friendly error messages for all validation failures

---

## Phase 3: Synthesis

**Purpose**: Toggle Complete functionality, integration, and UI polish

**Checkpoint**: All 5 features complete and integrated

- [x] T019 Implement toggle_complete() method in TaskService (validates ID exists, flips completed status)
- [x] T020 Connect Toggle Complete option in menu to toggle_complete()
- [x] T021 Install colorama dependency
- [x] T022 Add colored terminal output using colorama (✔ for complete, ✖ for incomplete)
- [x] T023 Add color highlighting for menu options
- [x] T024 Integrate all features into CLI menu for smooth workflow
- [ ] T025 Run end-to-end testing: Add → View → Update → Delete → Toggle Complete
- [ ] T026 Verify all operations work without runtime errors

---

## Phase 4: Quality Validation

**Purpose**: Ensure project meets success criteria

**Checkpoint**: Ready for delivery

- [x] T027 Test invalid input handling (non-existent IDs, empty titles, invalid menu options)
- [x] T028 Verify all tasks run correctly in terminal
- [x] T029 Confirm project structure matches deliverables (/src, /specs history, README.md, CLAUDE.md, constitution)
- [x] T030 Create README.md with setup instructions and usage guide
- [x] T031 Verify CLAUDE.md contains proper Claude Code instructions
- [x] T032 Final validation against success criteria from spec.md

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Foundation)**: No dependencies - start here
- **Phase 2 (Analysis)**: Depends on Phase 1 completion
- **Phase 3 (Synthesis)**: Depends on Phase 2 completion
- **Phase 4 (Quality)**: Depends on Phase 3 completion

### Within Each Phase

- T001, T002 can run in parallel (different directories)
- T004, T005 can run in parallel (different files)
- T006 depends on T004 (Task model must exist first)
- T007 depends on T004 (Task model must exist first)
- T008, T009 depend on T006, T007 (service methods needed)
- T010 depends on T005 (TaskService must exist)
- T011 depends on T005 (TaskService must exist)
- T012, T013 depend on T010, T011 (service methods needed)
- T019 depends on T005 (TaskService must exist)
- T020 depends on T019 (toggle_complete method needed)
- T022, T023 depend on colorama installation (T021)
- T024 depends on T012, T013, T020 (all menu options connected)
- T025 depends on T024 (all features integrated)

### Parallel Opportunities

- T001, T002: Different directories, no dependencies
- T004, T005: Different files, no dependencies
- T006, T007: Different methods, no dependencies
- T010, T011: Different methods, no dependencies
- T014-T018: Different validations, can run in parallel
- T021-T023: Different UI features, can run in parallel

---

## Implementation Strategy

### Incremental Delivery

1. Complete Phase 1 → Test Add + View → MVP functional!
2. Complete Phase 2 → Test Update + Delete → All CRUD operations work
3. Complete Phase 3 → Test Toggle + colors → Complete feature set
4. Complete Phase 4 → Final validation → Ready for delivery

### Quality Gates (per phase)

**Phase 1 Complete When:**
- [ ] Project structure created per plan.md
- [ ] Task model implemented with all fields
- [ ] Add Task creates task with unique ID
- [ ] View Tasks displays all tasks correctly
- [ ] Menu shows Add and View options

**Phase 2 Complete When:**
- [ ] Update Task modifies task details correctly
- [ ] Delete Task removes task correctly
- [ ] Invalid ID shows error message
- [ ] Empty title rejected for Add/Update
- [ ] Invalid menu option reprompts user

**Phase 3 Complete When:**
- [ ] Toggle Complete changes status correctly
- [ ] Colored output displays (✔ / ✖)
- [ ] All 5 menu options work
- [ ] Smooth workflow between options
- [ ] No runtime errors in terminal

**Phase 4 Complete When:**
- [ ] All invalid inputs handled gracefully
- [ ] README.md created with instructions
- [ ] Project structure matches requirements
- [ ] All success criteria from spec.md met

---

## Notes

- [P] tasks = different files, no dependencies
- Commit after each phase completion
- Stop at checkpoints to validate phase independently
- All file paths should be relative to repository root
