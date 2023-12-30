#!/usr/bin/python3
"""This module defines the gui version of the todolist app
using the tkinter GUI module
also in combination with the customtkinter module for
better appearance
"""


# import moduels
from tkinter import *
import customtkinter as ctk
from CTkListbox import *
from tkinter import messagebox
from core import TodoAppCore
from datetime import datetime

# declare properties for widgets
font1 = ('Arial', 30, 'bold')
font2 = ('Arial', 18, 'bold')
font3 = ('Arial', 10, 'bold')
font4 = ("Helvetica", 18, 'bold')


class TodoAppGUI:
    """the base class for the todo list app GUI"""
    def __init__(self, app_core):
        self.app_core = app_core
        self.root = ctk.CTk()
        self.root.title("Daily Todo List App")
        self.root.config(bg='#09112e')

        # Load tasks from file
        self.app_core.load_tasks()

        # Store tasks in a set
        self.ongoing_tasks_set = set(self.app_core.get_ongoing_tasks())
        self.completed_tasks_set = set(self.app_core.get_completed_tasks())

        # Welcome Dialog
        # self.show_welcome_dialog()

        # Todolist Caption
        self.caption_label = ctk.CTkLabel(
            self.root, text="Todolist", font=font1,
            text_color='#fff', bg_color='#09112e')
        self.caption_label.pack(pady=10)

        # Ongoing Tasks Section
        self.ongoing_label = ctk.CTkLabel(
            self.root, text="Ongoing Tasks with Date (Today: {})".format(
                self.app_core.get_today_date()), font=font4,
            corner_radius=8, fg_color="#AA4A44", text_color="#fff")
        self.ongoing_label.pack()

        self.ongoing_tasks_listbox = CTkListbox(
            self.root, height=5, text_color='#09112e',
            bg_color='#09112e', font=('Helvetica', 14, 'bold'))
        self.ongoing_tasks_listbox.pack(fill="both", expand=True, padx=10)

        # Completed Tasks Section
        self.completed_label = ctk.CTkLabel(
            self.root, text="Completed Tasks with Date",
            fg_color="green", font=font4, text_color="#fff")
        self.completed_label.pack()

        self.completed_tasks_listbox = CTkListbox(
            self.root, height=5, text_color='#09112e',
            bg_color='#09112e', font=('Helvetica', 14, 'bold'))
        self.completed_tasks_listbox.pack(
            fill="both", expand=True, padx=10)
        self.root.geometry("600x600")
        self.mark_complete_button = ctk.CTkButton(
            self.root, text="Mark Complete",
            command=self.mark_complete, hover_color='green',
            font=('Helvetica', 14, 'bold'), fg_color="#000080",
            text_color="white")
        self.mark_complete_button.pack(side="right")

        self.remove_task_button = ctk.CTkButton(
            self.root, text="Remove Task",
            command=self.remove_task, font=('Helvetica', 14, 'bold'),
            hover_color='black', fg_color="#8B0000", text_color="white")
        self.remove_task_button.pack(side="right", padx=10)

        # Input Section
        self.input_label = ctk.CTkLabel(
            self.root, text="Enter Task:",
            font=font4, fg_color="#96061c",
            text_color='#fff',)
        self.input_label.pack(pady=10)

        self.task_entry = ctk.CTkEntry(
            self.root, font=font2, text_color='#000', fg_color='#fff',
            border_color='#fff', width=280, height=50)
        self.task_entry.pack(padx=20, pady=10)

        # Buttons Section
        self.add_task_button = ctk.CTkButton(
            self.root, font=('Helvetica', 14, 'bold'),
            text_color='#fff', text='Add Task', hover_color='#35530A',
            fg_color="green", corner_radius=8, width=120,
            command=self.add_task)
        self.add_task_button.pack(side="left", padx=20, pady=5)

        self.exit_button = ctk.CTkButton(
            self.root, text="Exit",
            command=self.root.destroy,
            font=('Helvetica', 14, 'bold'),
            hover_color='black',
            fg_color="#AA4A44", text_color="white")
        self.exit_button.pack(side="right")

        # Update task lists
        self.update_task_lists()
        # set window gemometry
        self.root.update_idletasks()
        width = self.root.winfo_reqwidth()
        height = self.root.winfo_reqheight()
        self.root.geometry(f"{width}x{height}")
        # Center the window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (width/2))
        y_cordinate = int((screen_height/2) - (height/2))
        self.root.geometry(f"{width}x{height}+{x_cordinate}+{y_cordinate}")

    # these methods here could be refactored to the core.py module later
    def show_welcome_dialog(self):
        """trying to create a dialog box which would show some information
        asking user about their current mood
        whatever the user choses, a message that relates with the mood is
        displayed to help motivate and light up their spirit
        """
        user_choice = messagebox.showinfo(
            "Welcome!", "Welcome! How are you doing today?\nChoose an option.",
            icon='question', type='yesnocancel')

        if user_choice == 'yes':
            self.show_motivational_quote("Positive")
        elif user_choice == 'no':
            self.show_motivational_quote("Negative")
        else:
            self.show_motivational_quote("Neutral")

    def show_motivational_quote(self, feeling):
        """the motivationla quote to be displayed based on feelings"""
        quotes = {
            "Positive": "Believe you can and you're halfway there.",
            "Negative": "Every day may not be good, but there's\
                something good in every day.",
            "Neutral": "You are never too old to set another \
                goal or to dream a new dream."
        }
        messagebox.showinfo(
            "Motivational Quote",
            f"{quotes[feeling]}\nYou've got this! Today is another day.")

    def add_task(self):
        """method to add task to the list box
        the effective one for thsi project
        """
        task = self.task_entry.get()
        if task and task not in self.ongoing_tasks_set:
            timestamp = datetime.now().strftime("%H:%M:%S")
            formatted_task = f"{task} (Created at: {timestamp})"
            self.app_core.add_task(formatted_task)  # Save the formatted task
            # self.app_core.add_task(task)
            self.app_core.save_tasks()
            self.ongoing_tasks_set.add(formatted_task)
            self.update_task_lists()
            self.task_entry.delete(0, END)

    def mark_complete(self):
        """method to selected task from listbox completed"""
        selected_task_indices = self.ongoing_tasks_listbox.curselection()
        if isinstance(selected_task_indices, int):
            # Convert to a tuple for consistency
            selected_task_indices = (selected_task_indices,)
        if selected_task_indices:
            selected_tasks = [
                self.ongoing_tasks_listbox.get(index)
                for index in selected_task_indices]
            for task in selected_tasks:
                if task in self.ongoing_tasks_set:
                    timestamp = datetime.now().strftime("%H:%M:%S")
                    completed_task = f"{task} (Completed at {timestamp})"
                    self.app_core.mark_complete(task)
                    self.app_core.save_tasks()
                    self.ongoing_tasks_set.remove(task)
                    self.completed_tasks_set.add(completed_task)
            self.update_task_lists()
        else:
            messagebox.showerror('Error', 'No task selected')

    def remove_task(self):
        """method to remove task from listbox"""
        ongoing_indices = self.ongoing_tasks_listbox.curselection()
        completed_indices = self.completed_tasks_listbox.curselection()

        if isinstance(ongoing_indices, int):
            ongoing_indices = (ongoing_indices,)
        if isinstance(completed_indices, int):
            completed_indices = (completed_indices,)

        if ongoing_indices:
            ongoing_tasks = [
                self.ongoing_tasks_listbox.get(index)
                for index in ongoing_indices]
            for task in ongoing_tasks:
                if task in self.ongoing_tasks_set:
                    if messagebox.askyesno(
                            "Remove Task",
                            f"Do you want to remove the task:\n{task}"):
                        self.app_core.remove_task(task)
                        self.app_core.save_tasks()
                        self.ongoing_tasks_set.discard(task)
            self.update_task_lists()

        elif completed_indices:
            completed_tasks = [
                self.completed_tasks_listbox.get(index)
                for index in completed_indices]
            for task in completed_tasks:
                if task in self.completed_tasks_set:
                    if messagebox.askyesno(
                            "Remove Task",
                            f"Do you want to remove the task:\n{task}"):
                        self.app_core.remove_task(task)
                        self.app_core.save_tasks()
                        self.completed_tasks_set.discard(task)
            self.update_task_lists()

        else:
            messagebox.showerror('Error', 'No task selected')

    def update_task_lists(self):
        """method to update the state of the tasks list"""
        # Check if the listboxes are not empty before deleting
        if self.ongoing_tasks_listbox.size() > 0:
            self.ongoing_tasks_listbox.delete(0, 'END')
        if self.completed_tasks_listbox.size() > 0:
            self.completed_tasks_listbox.delete(0, END)

        # Insert tasks from the sets into the listboxes
        for task in self.ongoing_tasks_set:
            self.ongoing_tasks_listbox.insert(END, task)
        for task in self.completed_tasks_set:
            self.completed_tasks_listbox.insert(END, task)

    def run(self):
        """method to run the Tkinter event loop"""
        self.root.mainloop()


if __name__ == "__main__":
    window = Tk()
    app = TodoAppGUI(window)
    app.run()
