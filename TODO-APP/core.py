#!/usr/bin/python3
"""the core module that controls the data
manipulation aspect of the project
"""
from datetime import datetime


class TodoAppCore:
    """core class that creates an instance which gives
    access to the core methods for data manipulation
    """
    def __init__(self):
        """initializes class with tasks"""
        self.ongoing_tasks = []
        self.completed_tasks = []

    def get_today_date(self):
        """Get the current time"""
        return datetime.today().strftime("%d/%m/%Y")

    def add_task(self, task):
        """add task to the list"""
        self.ongoing_tasks.append(task)

    def mark_complete(self, task):
        """logic to mark completed task adding time frame also"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        completed_task = f"{task} (Completed at {timestamp})"
        self.completed_tasks.append(completed_task)
        self.ongoing_tasks.remove(task)

    def remove_task(self, task):
        """removes the ongoing task or compleeted task"""
        if task in self.ongoing_tasks:
            self.ongoing_tasks.remove(task)
        elif task in self.completed_tasks:
            self.completed_tasks.remove(task)

    def remove_task_from_lists(self, task):
        """removes selectd task from the task list"""
        if task in self.ongoing_tasks:
            self.ongoing_tasks.remove(task)

    def get_ongoing_tasks(self):
        """return ongoing tasks"""
        return self.ongoing_tasks

    def get_completed_tasks(self):
        """return completed task"""
        return self.completed_tasks

    def save_tasks(self):
        """save tasks to file txt file"""
        with open("tasks.txt", "w") as f:
            tasks = self.ongoing_tasks + self.completed_tasks
            for task in tasks:
                f.write(task + '\n')

    def load_tasks(self):
        """load created tasks from file"""
        try:
            with open("tasks.txt", "r") as f:
                tasks = f.readlines()
                for task in tasks:
                    if "(Completed at" not in task:
                        self.ongoing_tasks.append(task.strip())
                    else:
                        self.completed_tasks.append(task.strip())
        except FileNotFoundError:
            pass
