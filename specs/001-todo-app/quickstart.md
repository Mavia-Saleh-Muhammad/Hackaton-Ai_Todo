# Quickstart Guide: In-Memory Console Todo Application

**Date**: 2026-01-07
**Feature**: In-Memory Console Todo Application (Phase I)

## Getting Started

### Prerequisites
- Python 3.13+ installed
- Command-line access (terminal/command prompt)
- No external dependencies required

### Setup
1. Clone or download the repository
2. Navigate to the project directory
3. Ensure the `src/` directory contains `todo_app.py`

### Running the Application
```bash
cd src/
python todo_app.py
```

### Basic Usage
1. The application starts with a main menu
2. Select options by entering the corresponding number
3. Follow the on-screen prompts
4. Use option 6 to exit the application

### Available Features
1. **Add Task**: Creates a new task with title and optional description
2. **View Tasks**: Shows all tasks with ID, title, and completion status
3. **Update Task**: Modifies existing task title or description
4. **Delete Task**: Removes a task by its ID
5. **Mark Complete/Incomplete**: Toggles task completion status
6. **Exit**: Safely closes the application

### Sample Workflow
1. Start the application
2. Choose "Add Task" and enter a title
3. Optionally add a description
4. Choose "View Tasks" to see your list
5. Mark tasks as complete when finished
6. Continue managing tasks as needed

### Error Handling
- Invalid inputs will show error messages
- The application will not crash on incorrect input
- Empty task lists are handled gracefully
- Invalid task IDs will show appropriate error messages

### Limitations
- Data is stored in memory only (resets on application restart)
- No file or database persistence
- Single-user console interface only