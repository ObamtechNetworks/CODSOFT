#!/usr/bin/python3
"""this module defines the cli version of the todo list app"""


class TodoAppCLI:
    """the todo list cli verison base class"""
    def __init__(self, app_core):
        self.app_core = app_core

    def run(self):
        """keep running the menu options of for the cli version"""
        while True:
            self.show_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.mark_complete()
            elif choice == '3':
                self.remove_task()
            elif choice == '4':
                self.show_tasks()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    def show_menu(self):
        """show menu prompt for user to choose from"""
        print("\n=== CLI Todo App ===")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. Remove Task")
        print("4. Show Tasks")
        print("5. Exit")

    def add_task(self):
        """add the task to list"""
        task = input("Enter Task: ")
        self.app_core.add_task(task)

    def mark_complete(self):
        """mark completed task cli version"""
        task = input("Enter Task to mark as complete: ")
        self.app_core.mark_complete(task)

    def remove_task(self):
        """remove task"""
        task = input("Enter Task to remove: ")
        self.app_core.remove_task(task)

    def show_tasks(self):
        """show tasks both ongoing and completed"""
        print("\nOngoing Tasks:")
        for task in self.app_core.get_ongoing_tasks():
            print(task)

        print("\nCompleted Tasks:")
        for task in self.app_core.get_completed_tasks():
            print(task)
