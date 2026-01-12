---
id: 1
title: Create Todo Constitution
stage: constitution
date: 2026-01-07
surface: agent
model: claude-sonnet-4-5-20250929
feature: todo-app
branch: main
user: 3tee
command: sp.constitution
labels: [constitution, todo, spec]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - null
---

## Prompt

```
/sp.constitution

Project: In-Memory Console-Based Todo Application (Phase I)

Objective:
Build a clean, reliable, in-memory Python console Todo app that strictly follows software engineering fundamentals before any database, UI, or AI integration.

Tech Stack:
- Language: Python 3.x
- Runtime: Console / CLI
- Storage: In-memory only (no files, no DB, no external services)
- Tools: Claude Code, Spec-Kit compatible

Core Principles:
- Simplicity over cleverness (no over-engineering)
- Deterministic behavior (same input → same output)
- Explicit logic (no hidden side effects)
- Readability over brevity
- Zero external dependencies

Functional Requirements:
1. Add Task
   - Each task must have:
     - Unique ID (auto-increment or UUID)
     - Title (required, non-empty)
     - Optional description
     - Completion status (default: incomplete)

2. View Tasks
   - Display all tasks in a readable list
   - Clearly show ID, title, and completion status
   - Handle empty list gracefully

3. Update Task
   - Update title and/or description
   - Validate task existence before updating
   - Do NOT silently fail

4. Delete Task
   - Delete by task ID
   - Confirm existence before deletion

5. Mark Task as Complete / Incomplete
   - Toggle completion state
   - Explicit feedback after action

Non-Functional Requirements:
- No file system usage
- No database
- No async code
- No classes unless justified (functions preferred)
- No global mutable state without explanation
- Clear separation of concerns (menu logic vs task logic)

Error Handling Standards:
- Invalid input must be handled explicitly
- Program must never crash on bad user input
- User must always receive a clear error message

Code Quality Standards:
- Meaningful variable and function names
- Consistent formatting (PEP8)
- Inline comments ONLY where logic is non-obvious
- No dead code
- No unused variables or imports

CLI UX Standards:
- Clear menu options
- Loop-based interaction until user exits
- Explicit success and failure messages
- No confusing shortcuts or hidden commands

Constraints:
- Single Python file
- In-memory lifecycle: data resets on program restart
- Code must be beginner-readable but professional-grade

Out of Scope (STRICT):
- File saving
- Databases
- Web frameworks
- GUI
- AI features
- Authentication
- Testing frameworks (manual testing only)

Success Criteria:
- All listed features work correctly
- No unhandled exceptions
- Code can be extended later for Phase II (FastAPI + DB)
- Logic is clean enough to migrate to backend without rewrite
```

## Response snapshot

Created the constitution file for the in-memory console-based todo application with the following principles:

1. Simplicity Over Cleverness
2. Deterministic Behavior
3. Explicit Logic
4. Zero External Dependencies
5. Console-First Interface
6. Error Handling Standards

Added sections for functional requirements, code quality standards, and governance.

## Outcome

- ✅ Impact: Created constitution file with 6 core principles and governance structure
- 🧪 Tests: null
- 📁 Files: Updated .specify/memory/constitution.md
- 🔁 Next prompts: Next step is to implement the todo application following these principles
- 🧠 Reflection: Constitution clearly defines the constraints and principles for the todo application development

## Evaluation notes (flywheel)

- Failure modes observed: null
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Begin implementing the todo application according to the constitution