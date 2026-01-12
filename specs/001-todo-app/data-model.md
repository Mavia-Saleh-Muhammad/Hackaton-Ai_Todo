# Data Model: In-Memory Console Todo Application

**Date**: 2026-01-07
**Feature**: In-Memory Console Todo Application (Phase I)

## Core Entity: Task

### Fields
- **id** (int, required, immutable)
  - Unique identifier for the task
  - Auto-generated using incrementing counter
  - Used for all operations that require task identification

- **title** (str, required)
  - Task title/description (what needs to be done)
  - Must be non-empty string
  - Minimum length: 1 character

- **description** (str, optional)
  - Extended task details
  - Can be empty or None
  - Maximum length: 1000 characters (to prevent overly long inputs)

- **is_completed** (bool, required)
  - Completion status indicator
  - Default value: False (incomplete)
  - Boolean values only: True (completed) or False (incomplete)

### Validation Rules
1. Title must be a non-empty string (length > 0)
2. Description must be string or None (no type conversion attempted)
3. ID must be unique within the application session
4. is_completed must be boolean type
5. Task must exist before update/delete operations

### State Transitions
- Initial state: is_completed = False
- Transition to complete: is_completed = True
- Transition to incomplete: is_completed = False
- No other state transitions allowed

### Relationships
- No relationships with other entities (standalone entity)

## Data Storage Structure
- **In-memory storage**: List of Task dictionaries
- **Access pattern**: Sequential iteration for display, indexed lookup for operations
- **Lifetime**: Session-based (resets on application restart)
- **Size limitation**: Designed to handle up to 10,000 tasks efficiently

## Operations
1. **CREATE**: Add new task with auto-generated ID
2. **READ**: List all tasks or retrieve by ID
3. **UPDATE**: Modify title, description, or completion status by ID
4. **DELETE**: Remove task by ID
5. **TOGGLE**: Switch completion status by ID

## Constraints
- No duplicate IDs allowed
- No persistent storage (in-memory only)
- Thread-safe operations not required (single-user console application)
- No concurrent access concerns (console interface)