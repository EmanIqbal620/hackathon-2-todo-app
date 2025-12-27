<!--
Sync Impact Report:
- Version change: N/A → 1.0.0 (new constitution)
- Added principles: Accuracy, Clarity, Reproducibility, Rigor
- Added sections: Key Standards, Constraints, Success Criteria
- Templates requiring updates: None (templates are generic and compatible)
-->

# Todo CLI App Constitution

## Core Principles

### I. Accuracy
All task operations MUST work exactly as specified (Add, List, Update, Delete, Toggle Complete).
Variable and function names MUST reflect their purpose clearly.

**Rationale**: User trust depends on consistent, predictable behavior. Incorrect implementations
lead to data loss and frustration.

### II. Clarity
Code MUST be clean, readable, and maintainable. Function and variable names MUST reflect purpose
clearly.

**Rationale**: Future maintainers (including the original author) need to understand the codebase
quickly. Readable code reduces bugs and accelerates feature development.

### III. Reproducibility
Results of all actions (adding, updating, deleting, toggling tasks) MUST be consistent across
sessions.

**Rationale**: Users expect the same behavior every time they run the application. Inconsistent
behavior undermines confidence and makes debugging difficult.

### IV. Rigor (NON-NEGOTIABLE)
Application MUST strictly follow the spec; no extra features, no database, no external APIs.

**Rationale**: Scope creep introduces complexity and risk. Following the spec ensures on-time
delivery and prevents feature bloat. Additional features belong in future phases.

### V. Simplicity
Every feature MUST be implemented in the simplest way that satisfies the requirements. Avoid
over-engineering, premature abstraction, and speculative functionality.

**Rationale**: Simple code is easier to test, debug, and maintain. YAGNI (You Aren't Gonna Need It)
principles prevent wasted effort on features that may never be used.

## Key Standards

- **Python version**: 3.13+
- **Storage**: In-memory only (list of tasks)
- **CLI interface**: Terminal-only, menu-driven
- **Task Model Fields**: `id` (int), `title` (string), `description` (string), `completed` (bool)
- **Menu Options**: Add, List, Update, Delete, Toggle Complete
- **UI**: Colored terminal output using colorama; symbols ✔ / ✖ for completion
- **Code quality**: Clean code principles; no unused code or features
- **Persistence**: None (tasks reset between runs)

## Constraints

**Prohibited Features:**
- Authentication
- Categories
- Priorities
- Due dates
- Database or file storage
- GUI or web interface

**Execution Environment:**
- Terminal only (no web, no GUI frameworks)

**Development Process:**
- MUST follow spec-driven development using Claude Code and Spec-Kit Plus
- All changes MUST be traceable to feature specifications

## Success Criteria

- All 5 basic features implemented correctly (Add, List, Update, Delete, Toggle Complete)
- Menu interface works and validates user input
- Task operations correctly handle invalid input (non-existent ID, empty title, etc.)
- Terminal output is clear, readable, and uses color to highlight status
- Application fully runs in terminal without errors
- Project structure follows Spec-Kit Plus conventions

## Governance

This constitution supersedes all other development practices for this project.

**Amendment Procedure:**
- Constitution changes MUST be documented with rationale
- Amendments require review and approval before merging
- Major changes MUST include a migration plan for existing work

**Compliance:**
- All PRs and reviews MUST verify constitution compliance
- Complexity deviations MUST be justified in the PR description
- Refer to `.specify/templates/` for development workflow guidance

**Versioning:**
- MAJOR: Backward incompatible governance changes or principle removals
- MINOR: New principles or materially expanded guidance
- PATCH: Clarifications, wording fixes, non-semantic refinements

**Version**: 1.0.0 | **Ratified**: 2025-12-27 | **Last Amended**: 2025-12-27
