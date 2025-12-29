# Feature Specification: Intermediate Level Todo CLI – Hackathon 2 Phase I

**Feature Branch**: `002-todo-intermediate`
**Created**: 2025-12-27
**Status**: Draft
**Input**: User description for intermediate todo CLI enhancement

## User Scenarios & Testing

### User Story 1 - Add Task with Priority and Category (Priority: P1)

Users need to create tasks with priority levels and categories for better organization.

**Why this priority**: Adding priority and category is fundamental to the intermediate upgrade—without it, filtering and sorting have no meaning.

**Independent Test**: Can be tested by adding a task with priority/category and verifying they appear correctly in the task list.

**Acceptance Scenarios**:

1. **Given** the application is running, **When** the user selects "Add Task" and enters title, **Then** they can select a priority (High/Medium/Low).
2. **Given** the application is running, **When** adding a task, **Then** they can select a category (Work/Home/Personal).
3. **Given** a task is created with priority and category, **When** viewing the task list, **Then** both fields are displayed correctly.

---

### User Story 2 - Search Tasks (Priority: P1)

Users need to search for tasks by keyword to quickly find specific items in their list.

**Why this priority**: Search is essential for usability when the task list grows beyond a handful of items.

**Independent Test**: Can be tested by adding multiple tasks with different titles and verifying search returns correct results.

**Acceptance Scenarios**:

1. **Given** tasks exist in the application, **When** the user selects "Search Tasks" and enters a keyword, **Then** only tasks matching the keyword are displayed.
2. **Given** tasks exist with descriptions, **When** searching by keyword, **Then** matches in both title and description are returned.
3. **Given** no tasks match the search, **When** the user searches, **Then** a "No results found" message is shown.

---

### User Story 3 - Filter Tasks (Priority: P2)

Users need to filter tasks by status, priority, or category to focus on specific subsets of their work.

**Why this priority**: Filtering helps users organize and prioritize their workload without removing tasks from the system.

**Independent Test**: Can be tested by creating tasks with different attributes and verifying filters return only matching tasks.

**Acceptance Scenarios**:

1. **Given** tasks exist with different statuses, **When** filtering by status (All/Active/Completed), **Then** only tasks matching the filter are shown.
2. **Given** tasks exist with different priorities, **When** filtering by priority (High/Medium/Low), **Then** only tasks with that priority are shown.
3. **Given** tasks exist with different categories, **When** filtering by category (Work/Home/Personal), **Then** only tasks with that category are shown.
4. **Given** multiple filters are selected, **When** applying filters, **Then** tasks matching all selected criteria are shown.

---

### User Story 4 - Sort Tasks (Priority: P2)

Users need to sort tasks by various criteria to organize their view according to their preferences.

**Why this priority**: Sorting helps users focus on what matters most—whether urgent deadlines or alphabetical organization.

**Independent Test**: Can be tested by creating tasks with different priorities/dates and verifying the sort order.

**Acceptance Scenarios**:

1. **Given** tasks exist, **When** sorting by priority, **Then** tasks are ordered High → Medium → Low.
2. **Given** tasks exist, **When** sorting alphabetically, **Then** tasks are ordered A → Z by title.
3. **Given** tasks exist, **When** selecting default sort, **Then** tasks are shown in creation order (newest first).

---

### User Story 5 - View Enhanced Task Table (Priority: P1)

Users need to view tasks in an enhanced table format with priority and category columns.

**Why this priority**: The polished UI is a key requirement of the intermediate upgrade—improves readability and information density.

**Independent Test**: Can be tested by adding tasks with different attributes and verifying the table displays all columns.

**Acceptance Scenarios**:

1. **Given** tasks exist, **When** viewing the task list, **Then** the table displays: ID, User ID, Title, Priority, Category, Status.
2. **Given** tasks exist, **When** viewing the task list, **Then** completed tasks show [X] and incomplete show [ ].
3. **Given** tasks have descriptions, **When** viewing the task list, **Then** descriptions may be shown in expanded view or tooltip.

---

### User Story 6 - Update Task with Priority and Category (Priority: P2)

Users need to modify the priority and category of existing tasks as their needs change.

**Why this priority**: Tasks evolve—priority and category may need adjustment over time.

**Independent Test**: Can be tested by updating a task's priority/category and verifying the changes.

**Acceptance Scenarios**:

1. **Given** a task exists, **When** selecting "Update Task", **Then** the user can change the priority.
2. **Given** a task exists, **When** selecting "Update Task", **Then** the user can change the category.
3. **Given** a task is updated, **When** viewing the task list, **Then** the new priority and category are reflected.

---

### Edge Cases

- Empty search results: How does the system handle searches with no matches?
- All filters cleared: What is the default view when no filters are selected?
- Duplicate categories: How are categories managed when adding new ones?
- Priority tie-breaking: When sorting by priority and tasks have the same priority, what is the secondary sort?

## Requirements

### Functional Requirements

- **FR-001**: System MUST allow users to set priority when adding a task (High/Medium/Low).
- **FR-002**: System MUST allow users to set category when adding a task (Work/Home/Personal).
- **FR-003**: System MUST display priority and category columns in the task list view.
- **FR-004**: System MUST allow users to search tasks by keyword (matches title and description).
- **FR-005**: System MUST filter tasks by status (All/Active/Completed).
- **FR-006**: System MUST filter tasks by priority (High/Medium/Low).
- **FR-007**: System MUST filter tasks by category (Work/Home/Personal).
- **FR-008**: System MUST support multiple active filters simultaneously.
- **FR-009**: System MUST sort tasks by priority (High → Medium → Low).
- **FR-010**: System MUST sort tasks alphabetically (A → Z by title).
- **FR-011**: System MUST sort tasks by creation date (newest first by default).
- **FR-012**: System MUST allow users to update priority of existing tasks.
- **FR-013**: System MUST allow users to update category of existing tasks.
- **FR-014**: System MUST maintain the polished boxed UI format.
- **FR-015**: System MUST preserve all Phase I features (Add, View, Update, Delete, Toggle Complete).

### Key Entities

- **Task**: Represents a single todo item with the following attributes:
  - `id`: Unique integer identifier, auto-incremented
  - `user_id`: Integer identifier for the user who owns the task
  - `title`: String containing the task name (required)
  - `description`: String containing additional details (optional)
  - `completed`: Boolean indicating whether the task is done
  - `priority`: Enum/string (High/Medium/Low)
  - `category`: Enum/string (Work/Home/Personal)

- **FilterCriteria**: Represents active filter settings:
  - `keyword`: Search string (optional)
  - `status`: All/Active/Completed
  - `priority`: High/Medium/Low/All
  - `category`: Work/Home/Personal/All

- **SortCriteria**: Represents sort order:
  - `field`: priority/title/date
  - `direction`: asc/desc

## Success Criteria

### Measurable Outcomes

- **SC-001**: Users can add tasks with priority and category in under 30 seconds.
- **SC-002**: Search returns results within 1 second of entering the keyword.
- **SC-003**: Filter operations display correct subset of tasks matching criteria.
- **SC-004**: Sort operations reorder the task list correctly according to selected criteria.
- **SC-005**: Task table displays all 6 columns: ID, User ID, Title, Priority, Category, Status.
- **SC-006**: All existing Phase I features (Add, Update, Delete, Toggle Complete, View) continue to work.
- **SC-007**: Terminal UI maintains polished appearance with boxes, colors, and consistent formatting.
- **SC-008**: Exit message displays "Allah Hafiz" as in Phase I.

## Assumptions

- Priority is required for new tasks with a default of "Medium".
- Category is required for new tasks with a default of "Personal".
- Search is case-insensitive.
- Filters can be combined (e.g., show only "High" priority "Work" tasks).
- Sort applies to the currently filtered list.
- No due dates are required for this phase (mentioned in original prompt but not prioritized).
- Existing tasks without priority/category will default to Medium/Personal when viewed.
