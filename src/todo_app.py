#!/usr/bin/env python3
"""
In-Memory Console Todo Application

A simple console-based todo application that stores tasks in memory only.
Data is lost when the application is restarted.
"""

import sys
from typing import Dict, List, Optional


class TaskManager:
    """Manages in-memory tasks with CRUD operations."""

    def __init__(self):
        """Initialize the task manager with an empty task list and ID counter."""
        self.tasks: List[Dict] = []
        self.next_id: int = 1

    def add_task(self, title: str, description: Optional[str] = None) -> Optional[int]:
        """
        Add a new task with the given title and optional description.

        Args:
            title: Required task title (must be non-empty)
            description: Optional task description

        Returns:
            The ID of the created task, or None if title is invalid
        """
        if not title or not title.strip():
            return None

        task = {
            'id': self.next_id,
            'title': title.strip(),
            'description': description.strip() if description else "",
            'is_completed': False
        }

        self.tasks.append(task)
        task_id = self.next_id
        self.next_id += 1

        return task_id

    def get_all_tasks(self) -> List[Dict]:
        """Return a copy of all tasks."""
        return self.tasks.copy()

    def get_task_by_id(self, task_id: int) -> Optional[Dict]:
        """
        Get a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The task dictionary if found, None otherwise
        """
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update a task's title and/or description.

        Args:
            task_id: The ID of the task to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            True if task was updated, False if task doesn't exist
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        if title is not None:
            if not title.strip():
                return False
            task['title'] = title.strip()

        if description is not None:
            task['description'] = description.strip() if description else ""

        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if task was deleted, False if task doesn't exist
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        self.tasks.remove(task)
        return True

    def toggle_task_completion(self, task_id: int) -> bool:
        """
        Toggle a task's completion status.

        Args:
            task_id: The ID of the task to toggle

        Returns:
            True if task status was toggled, False if task doesn't exist
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        task['is_completed'] = not task['is_completed']
        return True


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("         IN-MEMORY CONSOLE TODO APPLICATION")
    print("="*50)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete/Incomplete")
    print("6. Exit")
    print("-"*50)


def get_user_choice() -> str:
    """
    Get user's menu choice with error handling.

    Returns:
        The user's choice as a string
    """
    try:
        choice = input("Enter your choice (1-6): ").strip()
        return choice
    except (EOFError, KeyboardInterrupt):
        print("\n\nApplication interrupted. Exiting...")
        sys.exit(0)


def handle_add_task(task_manager: TaskManager):
    """Handle adding a new task."""
    print("\n--- ADD TASK ---")

    try:
        title = input("Enter task title: ").strip()

        if not title:
            print("ERROR: Task title cannot be empty!")
            return

        description_input = input("Enter task description (optional, press Enter to skip): ").strip()
        description = description_input if description_input else None

        task_id = task_manager.add_task(title, description)

        if task_id is not None:
            print(f"SUCCESS: Task added successfully! ID: {task_id}")
        else:
            print("ERROR: Failed to add task - title cannot be empty!")

    except (EOFError, KeyboardInterrupt):
        print("\nOperation cancelled.")
        return


def handle_view_tasks(task_manager: TaskManager):
    """Handle viewing all tasks."""
    print("\n--- VIEW TASKS ---")

    tasks = task_manager.get_all_tasks()

    if not tasks:
        print("INFO: No tasks found. Your list is empty!")
        return

    print(f"INFO: Found {len(tasks)} task(s):\n")

    for task in tasks:
        status = "[DONE]" if task['is_completed'] else "[PENDING]"
        print(f"ID: {task['id']:3d} | {status} | {task['title']}")

        if task['description']:
            print(f"         Description: {task['description']}")
        print()


def handle_update_task(task_manager: TaskManager):
    """Handle updating an existing task."""
    print("\n--- UPDATE TASK ---")

    if not task_manager.get_all_tasks():
        print("INFO: No tasks available to update!")
        return

    try:
        task_id_str = input("Enter task ID to update: ").strip()
        task_id = int(task_id_str)

        task = task_manager.get_task_by_id(task_id)
        if not task:
            print(f"ERROR: Task with ID {task_id} not found!")
            return

        print(f"Current task: {task['title']}")
        if task['description']:
            print(f"Current description: {task['description']}")

        new_title = input("Enter new title (press Enter to keep current): ").strip()
        new_title = new_title if new_title else None

        new_desc = input("Enter new description (press Enter to keep current): ").strip()
        new_desc = new_desc if new_desc else None

        # If user entered an empty string for description, treat as intentional empty
        if input("Press Enter to keep current description, or type anything to update: ") != "":
            new_desc = input("Enter new description: ").strip()
            if not new_desc:  # If they enter an empty string, set to None
                new_desc = None

        success = task_manager.update_task(task_id, new_title, new_desc)

        if success:
            print("SUCCESS: Task updated successfully!")
        else:
            print("ERROR: Failed to update task!")

    except ValueError:
        print(f"ERROR: '{task_id_str}' is not a valid task ID!")
    except (EOFError, KeyboardInterrupt):
        print("\nOperation cancelled.")


def handle_delete_task(task_manager: TaskManager):
    """Handle deleting a task."""
    print("\n--- DELETE TASK ---")

    if not task_manager.get_all_tasks():
        print("INFO: No tasks available to delete!")
        return

    try:
        task_id_str = input("Enter task ID to delete: ").strip()
        task_id = int(task_id_str)

        task = task_manager.get_task_by_id(task_id)
        if not task:
            print(f"ERROR: Task with ID {task_id} not found!")
            return

        print(f"You are about to delete: {task['title']}")
        confirm = input("Confirm deletion (y/N): ").strip().lower()

        if confirm in ['y', 'yes']:
            success = task_manager.delete_task(task_id)
            if success:
                print("SUCCESS: Task deleted successfully!")
            else:
                print("ERROR: Failed to delete task!")
        else:
            print("ERROR: Deletion cancelled.")

    except ValueError:
        print(f"ERROR: '{task_id_str}' is not a valid task ID!")
    except (EOFError, KeyboardInterrupt):
        print("\nOperation cancelled.")


def handle_toggle_task(task_manager: TaskManager):
    """Handle toggling a task's completion status."""
    print("\n--- MARK TASK COMPLETE/INCOMPLETE ---")

    if not task_manager.get_all_tasks():
        print("INFO: No tasks available!")
        return

    try:
        task_id_str = input("Enter task ID to toggle: ").strip()
        task_id = int(task_id_str)

        task = task_manager.get_task_by_id(task_id)
        if not task:
            print(f"ERROR: Task with ID {task_id} not found!")
            return

        current_status = "COMPLETED" if task['is_completed'] else "INCOMPLETE"
        new_status = "INCOMPLETE" if task['is_completed'] else "COMPLETED"

        print(f"Task: {task['title']}")
        print(f"Current status: {current_status}")
        print(f"After toggle: {new_status}")

        confirm = input("Confirm toggle (y/N): ").strip().lower()

        if confirm in ['y', 'yes']:
            success = task_manager.toggle_task_completion(task_id)
            if success:
                new_status = "COMPLETED" if task['is_completed'] else "INCOMPLETE"
                print(f"SUCCESS: Task marked as {new_status}!")
            else:
                print("ERROR: Failed to toggle task status!")
        else:
            print("ERROR: Toggle cancelled.")

    except ValueError:
        print(f"ERROR: '{task_id_str}' is not a valid task ID!")
    except (EOFError, KeyboardInterrupt):
        print("\nOperation cancelled.")


def main():
    """Main application loop."""
    print("Starting In-Memory Console Todo Application...")
    print("Note: Data is stored in memory only and will reset when the application restarts.")

    task_manager = TaskManager()

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':
            handle_add_task(task_manager)
        elif choice == '2':
            handle_view_tasks(task_manager)
        elif choice == '3':
            handle_update_task(task_manager)
        elif choice == '4':
            handle_delete_task(task_manager)
        elif choice == '5':
            handle_toggle_task(task_manager)
        elif choice == '6':
            print("\nThank you for using the In-Memory Console Todo Application!")
            print("Remember: All data is stored in memory and will be lost when the application closes.")
            print("Goodbye!")
            sys.exit(0)
        else:
            print(f"\nERROR: Invalid choice: '{choice}'. Please enter a number between 1 and 6.")

        # Pause to let user see the result before showing menu again
        try:
            input("\nPress Enter to continue...")
        except (EOFError, KeyboardInterrupt):
            print("\nApplication interrupted. Exiting...")
            sys.exit(0)


if __name__ == "__main__":
    main()