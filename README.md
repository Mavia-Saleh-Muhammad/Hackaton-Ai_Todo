# In-Memory Console Todo Application

A simple, clean, and reliable console-based todo application built in Python. This application stores all tasks in memory only, making it perfect for temporary task management without any persistence requirements.

## Features

- ✅ Add new tasks with titles and optional descriptions
- ✅ View all tasks with clear status indicators
- ✅ Update existing tasks (title and description)
- ✅ Delete tasks by ID
- ✅ Mark tasks as complete/incomplete
- ✅ User-friendly console interface
- ✅ Robust error handling
- ✅ In-memory storage (no files or databases)

## Setup Instructions

1. Ensure you have Python 3.13+ installed on your system
2. Clone or download this repository
3. Navigate to the project directory

## How to Run the Application

1. Open your terminal/command prompt
2. Navigate to the project directory
3. Run the following command:

```bash
python src/todo_app.py
```

## Expected Behavior

- **In-Memory Only**: All data is stored in memory and will reset when the application is closed and reopened
- **No Persistence**: No files are created or modified on your system
- **Console Interface**: Simple menu-driven interface for easy task management
- **Error Handling**: The application handles invalid inputs gracefully without crashing

## Usage

The application provides a simple menu system:

1. **Add Task**: Create new tasks with titles and optional descriptions
2. **View Tasks**: See all tasks with their IDs and completion status
3. **Update Task**: Modify existing task titles or descriptions
4. **Delete Task**: Remove tasks by their ID
5. **Mark Complete/Incomplete**: Toggle task completion status
6. **Exit**: Safely close the application

## Technical Details

- Built with Python 3.13+ standard library only (no external dependencies)
- Follows clean code principles and PEP8 formatting
- Single-file implementation for simplicity
- Separation of concerns between business logic and CLI interface
- Comprehensive error handling for invalid inputs

## Limitations

- Data is not persisted between application runs
- Single-user console application
- No network or file system access