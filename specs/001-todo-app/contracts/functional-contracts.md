# API Contracts: In-Memory Console Todo Application

**Date**: 2026-01-07
**Feature**: In-Memory Console Todo Application (Phase I)

## Overview
This document outlines the functional contracts for the console todo application. Since this is a console application, these represent the functional interfaces and expected behaviors rather than traditional API endpoints.

## Core Operations

### 1. Add Task
**Function**: `add_task(title: str, description: str = None) -> dict`
**Purpose**: Create a new task with auto-generated ID and incomplete status
**Input**:
- title (str, required): Task title (non-empty)
- description (str, optional): Task description
**Output**:
- task (dict): Complete task object with ID
**Errors**:
- ValueError: If title is empty
- TypeError: If title is not a string

### 2. View All Tasks
**Function**: `view_tasks() -> list`
**Purpose**: Retrieve all tasks in the system
**Input**: None
**Output**:
- tasks (list): List of all task dictionaries
**Special Case**:
- Returns empty list if no tasks exist

### 3. Update Task
**Function**: `update_task(task_id: int, title: str = None, description: str = None) -> bool`
**Purpose**: Modify an existing task's title or description
**Input**:
- task_id (int): ID of task to update
- title (str, optional): New title value
- description (str, optional): New description value
**Output**:
- success (bool): True if update successful, False otherwise
**Errors**:
- ValueError: If task_id doesn't exist

### 4. Delete Task
**Function**: `delete_task(task_id: int) -> bool`
**Purpose**: Remove a task from the system
**Input**:
- task_id (int): ID of task to delete
**Output**:
- success (bool): True if deletion successful, False otherwise
**Errors**:
- ValueError: If task_id doesn't exist

### 5. Toggle Task Status
**Function**: `toggle_task_status(task_id: int) -> bool`
**Purpose**: Switch task completion status
**Input**:
- task_id (int): ID of task to update
**Output**:
- success (bool): True if status toggled, False otherwise
**Errors**:
- ValueError: If task_id doesn't exist

### 6. Get Task by ID
**Function**: `get_task_by_id(task_id: int) -> dict`
**Purpose**: Retrieve a specific task
**Input**:
- task_id (int): ID of task to retrieve
**Output**:
- task (dict): Task object if found
**Errors**:
- ValueError: If task_id doesn't exist

## Data Contract

### Task Object
```python
{
    "id": int,           # Unique identifier (immutable)
    "title": str,        # Task title (required, non-empty)
    "description": str,  # Task description (optional, can be None)
    "is_completed": bool # Completion status (required)
}
```

## Error Handling Contract
All functions follow the same error handling pattern:
- Invalid inputs raise ValueError with descriptive message
- Non-existent tasks raise ValueError with descriptive message
- Type errors raise TypeError with descriptive message
- Successful operations return appropriate success indicators