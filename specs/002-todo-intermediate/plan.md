# Implementation Plan: Intermediate Level Todo CLI – Hackathon 2 Phase I

**Branch**: `002-todo-intermediate` | **Date**: 2025-12-27 | **Spec**: [spec.md](../spec.md)
**Input**: Feature specification from `/specs/002-todo-intermediate/spec.md`

## Summary

Enhance the existing Todo CLI app with priority levels (High/Medium/Low), categories (Work/Home/Personal), search functionality, filter options, and sort capabilities while maintaining the polished boxed terminal UI. The architecture extends the existing Phase I structure with additional Task model fields and enhanced TaskService methods.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: colorama (colored terminal output)
**Storage**: In-memory Python list (no persistence, extended from Phase I)
**Testing**: Manual validation during development
**Target Platform**: Terminal/Console (cross-platform)
**Project Type**: Single CLI application (extends Phase I)
**Performance Goals**: Responsive CLI (search/filter under 1 second)
**Constraints**: In-memory only, no database, terminal-only, preserve Phase I features
**Scale/Scope**: Single user, local execution, extends existing codebase

## Constitution Check

*GATE: Must pass before implementation. Re-check after design.*

| Principle | Requirement | Compliance |
|-----------|-------------|------------|
| I. Accuracy | Task operations work as specified | ✅ Extended with priority/category in all operations |
| II. Clarity | Clean, readable code with clear names | ✅ New fields documented, meaningful names preserved |
| III. Reproducibility | Consistent behavior | ✅ Search/filter/sort deterministic |
| IV. Rigor | No extra features, no database | ⚠️ **Constitution Amendment Required** - Categories and Priorities are now explicitly allowed for Phase II |
| V. Simplicity | Simplest implementation | ✅ In-memory filtering/sorting, no external libraries |

**Constitution Note for Phase II**: The original constitution listed Categories and Priorities as prohibited features for Phase I. Phase II explicitly adds these features as enhancement requirements. This is a planned scope expansion, not scope creep.

## Project Structure

### Documentation (this feature)

```text
specs/002-todo-intermediate/
├── plan.md              # This file (/sp.plan command output)
├── spec.md              # Feature specification (/sp.spec output)
└── tasks.md             # Phase 2 output (/sp.tasks command)
```

### Source Code (repository root)

```text
src/
├── __init__.py
├── main.py              # Application entry point (updated)
├── models/
│   ├── __init__.py
│   └── task.py          # Task dataclass (updated: added priority, category)
├── services/
│   ├── __init__.py
│   └── task_service.py  # TaskService (updated: search, filter, sort methods)
└── cli/
    ├── __init__.py
    └── menu.py          # Menu interface (updated: enhanced table, new menu options)
```

**Structure Decision**: Single project extending Phase I structure. Task model gets new fields, TaskService gets new methods, Menu gets new options and enhanced table display.

## Decisions

| Decision | Options | Tradeoffs | Chosen |
|----------|---------|-----------|--------|
| Priority representation | Enum class vs string vs int | Enum type-safe but more code; string simple; int sortable | String (High/Medium/Low) |
| Category representation | Enum class vs string vs list | Enum for type safety; string simple; list for multiple | String (Work/Home/Personal) |
| Search scope | Title only vs title+description | Title only faster; both more comprehensive | Title + description |
| Filter combination | OR (any match) vs AND (all match) | OR shows more results; AND more restrictive | AND (all criteria) |
| Sort order for priority | H→M→L vs L→M→H | High first emphasizes urgency | High → Medium → Low |

## Complexity Tracking

> **Constitution Amendment for Phase II**: Categories and Priorities are now explicitly allowed as they are Phase II enhancement requirements. All other constraints (no database, no persistence, terminal-only) remain in effect.

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Categories (Phase I prohibited) | Phase II requirement for task organization | Cannot achieve filtering without categories |
| Priorities (Phase I prohibited) | Phase II requirement for task sorting | Cannot achieve priority sorting without priority field |

## Implementation Phases

### Phase 1: Data Model Enhancement

**Goal**: Update Task model with priority and category fields

1. Add `priority` field to Task dataclass (High/Medium/Low, default Medium)
2. Add `category` field to Task dataclass (Work/Home/Personal, default Personal)
3. Update TaskService.add_task() to accept priority and category parameters
4. Add `updated_flag` field to track modified tasks (per architecture sketch)

### Phase 2: Search & Filter Implementation

**Goal**: Enable finding and narrowing down tasks

1. Add `search_tasks()` method to TaskService (keyword search in title + description)
2. Add `filter_tasks()` method to TaskService (status, priority, category filters)
3. Support combinable filters (AND logic)
4. Case-insensitive search

### Phase 3: Sort Implementation

**Goal**: Allow reordering tasks by different criteria

1. Add `sort_tasks()` method to TaskService
2. Implement sort by priority (High → Medium → Low)
3. Implement sort alphabetically (A → Z)
4. Implement sort by creation date (newest first)

### Phase 4: Enhanced UI

**Goal**: Display tasks with priority/category in polished table format

1. Update task table display to show: ID, User ID, Title, Priority, Category, Status
2. Add color coding for priority (High=Red, Medium=Yellow, Low=Green)
3. Add menu options for Search, Filter, Sort
4. Maintain existing boxed UI format (welcome, feedback, exit boxes)

### Phase 5: Integration & Testing

**Goal**: Connect new features to menu and test end-to-end

1. Connect Add Task to accept priority/category input
2. Connect Update Task to modify priority/category
3. Add Search, Filter, Sort menu options
4. Test all Phase I features still work
5. Test new Phase II features work correctly

## Testing Strategy

### Validation Checks

| Feature | Check |
|---------|-------|
| Add Task with Priority/Category | Task created with correct priority and category |
| Search | Returns tasks matching keyword in title or description |
| Filter Status | Shows only All/Active/Completed tasks as selected |
| Filter Priority | Shows only tasks with selected priority |
| Filter Category | Shows only tasks with selected category |
| Sort Priority | Tasks ordered High → Medium → Low |
| Sort Alphabetically | Tasks ordered A → Z by title |
| Sort Date | Tasks ordered newest first |
| Enhanced Table | All 6 columns display correctly |
| Phase I Features | Add/Update/Delete/Toggle still work |

### End-to-End Checks

- Run through all 5 phases sequentially
- Verify app runs in terminal without errors
- Confirm colored output displays correctly
- Test search with various keyword combinations
- Test filter combinations work correctly

## Quality Gates

Before marking each phase complete:

1. ✅ Code follows clean code principles (Clarity)
2. ✅ No unused code or features (Rigor)
3. ✅ All operations work as specified (Accuracy)
4. ✅ User input is validated (Reproducibility)
5. ✅ Terminal output is clear and colored (Clarity)
6. ✅ Phase I features remain functional (Backward Compatibility)
