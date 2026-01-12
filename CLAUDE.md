# Claude Code Usage Instructions

This document provides instructions for using Claude Code with the In-Memory Console Todo Application project.

## About This Project

This is a spec-driven development project for an in-memory console-based todo application. The application follows strict clean code principles and uses only Python standard library components.

## Spec-Driven Development Workflow

This project follows the spec-driven development approach using Claude Code and Spec-Kit Plus:

1. **Constitution** (`/sp.constitution`): Establishes core principles and constraints
2. **Specification** (`/sp.specify`): Defines user scenarios and requirements
3. **Planning** (`/sp.plan`): Creates technical architecture and design
4. **Tasks** (`/sp.tasks`): Breaks down implementation into atomic tasks
5. **Implementation** (`/sp.implement`): Executes the implementation plan

## How to Execute Claude Code

### Initial Setup
1. Ensure Python 3.13+ is installed
2. Navigate to the project directory
3. All source code is located in the `/src` directory

### Running the Application
```bash
python src/todo_app.py
```

### Available Commands (using Claude Code + Spec-Kit Plus)

- `/sp.constitution` - Update project constitution and principles
- `/sp.specify` - Create or update feature specifications
- `/sp.plan` - Generate implementation plans
- `/sp.tasks` - Break down implementation into tasks
- `/sp.implement` - Execute implementation based on tasks

## Project Structure

```
project-root/
├── src/
│   └── todo_app.py          # Main application
├── specs/
│   └── 001-todo-app/       # Feature specifications
│       ├── spec.md
│       ├── plan.md
│       ├── tasks.md
│       ├── research.md
│       ├── data-model.md
│       ├── quickstart.md
│       └── contracts/
├── README.md               # Setup and usage instructions
├── CLAUDE.md               # Claude Code usage instructions
└── .specify/               # Spec-Kit configuration
```

## Development Guidelines

### Code Quality Standards
- Follow PEP8 formatting
- Use meaningful variable and function names
- Include minimal comments (only for non-obvious logic)
- Avoid unused imports or variables
- Prefer functions over classes unless justified

### Architecture Constraints
- In-memory storage only (no files or databases)
- Console-based interface only
- Python standard library only (no external dependencies)
- Single file implementation for simplicity
- No async or multi-threaded code

### Error Handling
- Never crash on invalid input
- Provide clear success/error feedback
- Validate all user inputs
- Handle edge cases gracefully

## Phase I Scope

This project is currently in Phase I, which includes:
- Add Task functionality
- View Tasks functionality
- Update Task functionality
- Delete Task functionality
- Mark Task Complete/Incomplete functionality
- Console-based user interface
- In-memory storage only

## Extending the Application

Future phases may include:
- Web interface (Phase II)
- Database persistence (Phase III)
- Authentication (Phase IV)
- Advanced features (Phase V)

## Troubleshooting

If you encounter issues:
1. Verify Python 3.13+ is installed
2. Check that you're running from the project root directory
3. Ensure the `src/todo_app.py` file exists
4. Confirm no syntax errors in the code