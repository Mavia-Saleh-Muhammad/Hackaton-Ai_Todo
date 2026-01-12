---
description: "Task list for In-Memory Console Todo Application"
---

# Tasks: In-Memory Console Todo Application

**Input**: Design documents from `/specs/001-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan
- [x] T002 Create src/ directory for main application
- [x] T003 [P] Create README.md with setup instructions
- [x] T004 [P] Create CLAUDE.md with Claude Code usage instructions

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T005 Create in-memory data structure for tasks with auto-incrementing IDs
- [x] T006 [P] Implement task model with ID, title, description, and completion status
- [x] T007 [P] Setup console interface with clear menu options
- [x] T008 Create base functions for task operations (add, view, update, delete, mark complete)
- [x] T009 Configure error handling to prevent crashes on invalid input
- [x] T010 Setup main application loop for user interaction

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Tasks (Priority: P1) 🎯 MVP

**Goal**: Allow users to add new tasks with title and optional description

**Independent Test**: User can add a task and see it in the task list with a unique ID and incomplete status

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T011 [P] [US1] Test that adding a task with valid title creates a new task in the in-memory store
- [ ] T012 [P] [US1] Test that adding a task with empty title shows appropriate error message

### Implementation for User Story 1

- [x] T013 [P] [US1] Create task creation function in src/todo_app.py that validates title is not empty
- [x] T014 [P] [US1] Implement auto-incrementing ID generation for new tasks
- [x] T015 [US1] Add console interface for task creation (input prompts and validation)
- [x] T016 [US1] Implement error handling for empty title input
- [x] T017 [US1] Add success feedback when task is created successfully
- [x] T018 [US1] Update main menu to include option for adding tasks

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Tasks (Priority: P2)

**Goal**: Allow users to view all tasks with ID, title, and completion status

**Independent Test**: User can view a list of all tasks in a readable format

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T019 [P] [US2] Test that viewing tasks shows all tasks with ID, title, and completion status
- [ ] T020 [P] [US2] Test that viewing tasks shows appropriate message when no tasks exist

### Implementation for User Story 2

- [x] T021 [P] [US2] Create task listing function in src/todo_app.py that formats tasks for display
- [x] T022 [US2] Implement console interface for displaying tasks in readable format
- [x] T023 [US2] Add logic to handle empty task list with appropriate message
- [x] T024 [US2] Update main menu to include option for viewing tasks

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update and Manage Tasks (Priority: P3)

**Goal**: Allow users to update task details, mark tasks as complete/incomplete, or delete tasks

**Independent Test**: User can update a task's title/description, mark it as complete/incomplete, or delete it by specifying the task ID

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T025 [P] [US3] Test that updating a task with valid ID modifies the task correctly
- [ ] T026 [P] [US3] Test that updating a task with invalid ID shows appropriate error message
- [ ] T027 [P] [US3] Test that deleting a task with valid ID removes it from memory
- [ ] T028 [P] [US3] Test that marking a task complete/incomplete updates its status correctly

### Implementation for User Story 3

- [x] T029 [P] [US3] Create task update function in src/todo_app.py that modifies title and description
- [x] T030 [P] [US3] Create task deletion function in src/todo_app.py that removes task by ID
- [x] T031 [P] [US3] Create task status toggle function in src/todo_app.py that switches completion status
- [x] T032 [US3] Implement validation to confirm task exists before update/delete operations
- [x] T033 [US3] Add console interface for task update functionality
- [x] T034 [US3] Add console interface for task deletion functionality
- [x] T035 [US3] Add console interface for task status toggle functionality
- [x] T036 [US3] Update main menu to include options for updating, deleting, and marking tasks

**Checkpoint**: At this point, all user stories should be independently functional

---

[Add more user story phases as needed, following the same pattern]

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T037 [P] Documentation updates in README.md
- [x] T038 Code cleanup and refactoring
- [x] T039 [P] Additional validation for edge cases (long titles, special characters)
- [x] T040 [P] Final testing of all features together
- [x] T041 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Test that adding a task with valid title creates a new task in the in-memory store"
Task: "Test that adding a task with empty title shows appropriate error message"

# Launch all implementation tasks for User Story 1 together:
Task: "Create task creation function in src/todo_app.py that validates title is not empty"
Task: "Implement auto-incrementing ID generation for new tasks"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence