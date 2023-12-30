# TODO List App

- **WHITEBOARD TOOL / LINK TO BOARD** : [WHIMSICAL](https://whimsical.com/todo-list-5DWh5wJWEbtft6ZZG2rvLX)
## [FLOWCHART AND UI DESIGN](https://github.com/ObamtechNetworks/CODSOFT/blob/main/TODO-APP/screenshots/flowchart%20and%20UI%20Design.png)

## TODO LIST GUI SCREENSHOT
### main window
![TODO APP GUI](https://github.com/ObamtechNetworks/CODSOFT/blob/main/TODO-APP/screenshots/main%20window.png)

## Project Overview

This TODO List App is a simple yet effective task management application that provides both Command Line Interface (CLI) and Graphical User Interface (GUI) options. It allows users to add, mark as complete, remove, and view tasks, providing a flexible and user-friendly experience.

## Table of Contents

- [Project Overview](#project-overview)
- [Table of Contents](#table-of-contents)
- [Features](#features)
- [Project Structure](#project-structure)
- [How to Use](#how-to-use)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [Author](#author)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## Features

- **CLI and GUI:** Choose between a command-line interface or a graphical user interface based on your preference.

- **Add Task:** Easily add new tasks to the ongoing task list.

- **Mark as Complete:** Mark tasks as complete with the ability to view completion timestamps.

- **Remove Task:** Remove tasks from the ongoing or completed task lists.

- **View Tasks:** View both ongoing and completed tasks for better organization.

- **Persistence:** Save tasks to a file (`tasks.txt`) for data persistence.

## Project Structure

The project is structured into the following components:

- **`main.py`:** Entry point of the application, allowing users to choose between CLI and GUI.

- **`cli.py`:** CLI version of the TODO List App, handling user interactions through the command line.

- **`gui.py`:** GUI version of the TODO List App, utilizing Tkinter for graphical user interactions.

- **`core.py`:** Core module handling the data manipulation and task-related logic.

- **`models.py`:** Module responsible for handling file storage and loading tasks from a file.

## How to Use

### Getting Started

To get started with the TODO List App, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ObamtechNetworks/CODSOFT.git
   ```

### Navigate to the Project Directory:

```bash
cd CODSOFT/TODO-APP
```

### **Install Dependencies (if needed):**

```bash
pip install -r requirements.txt
```
#### Run the App:

# For CLI Version:

```bash
python3 main.py
```
Choose 'cli' when prompted.

# For GUI Version:

```bash
python3 main.py
```
Choose 'gui' when prompted.


## TODO LIST GUI SCREENSHOT
### main window
![TODO APP GUI](https://github.com/ObamtechNetworks/CODSOFT/blob/main/TODO-APP/screenshots/main%20window.png)

### enter task
![ENTER TASK](https://github.com/ObamtechNetworks/CODSOFT/blob/main/TODO-APP/screenshots/GUI%20add_to_input_list_box.png)

### select task
![SELECT TASK](https://github.com/ObamtechNetworks/CODSOFT/blob/main/TODO-APP/screenshots/GUI%20select_task.png)

### mark task completed
![MARK TASK COMPLETED](https://github.com/ObamtechNetworks/CODSOFT/blob/main/TODO-APP/screenshots/Mark%20task%20completed.png)

### remove unfinished task
![REMOVE UNFINISHED TASK](https://github.com/ObamtechNetworks/CODSOFT/blob/main/TODO-APP/screenshots/remove%20unfinsihed%20task.png)

### remove completed task
![REMOVE COMPLETED TASK](https://github.com/ObamtechNetworks/CODSOFT/blob/main/TODO-APP/screenshots/remove%20completed%20task.png)

### GUI created tasks persists
![CREATED TASK PERSISTS GUI](https://github.com/ObamtechNetworks/CODSOFT/blob/main/TODO-APP/screenshots/created%20task_persists.png)

# CLI Version
- Open a terminal.
- Navigate to the project directory.

- Run the following command:

```bash
python3 main.py
```

## TODO LIST CLI SCREENSHOTS
### main window
![TODO APP CLI](https://github.com/ObamtechNetworks/CODSOFT/blob/main/TODO-APP/screenshots/cli%20version%20main.png)

### add task
![ADD TASK](https://github.com/ObamtechNetworks/CODSOFT/blob/main/TODO-APP/screenshots/add%20tasks.png)

### ongoing task
![ONGOING TASK](https://github.com/ObamtechNetworks/CODSOFT/blob/main/TODO-APP/screenshots/ongoing%20tasks2.png)

### mark task completed
![MARK TASK COMPLETED](https://postimg.cc/pykDb815)

### completed task
![MORE TASK](https://github.com/ObamtechNetworks/CODSOFT/blob/main/TODO-APP/screenshots/mark%20task%20completed_cli.png)

### remove completed task
![EXIT](https://github.com/ObamtechNetworks/CODSOFT/blob/main/TODO-APP/screenshots/exit%20cli.png)

# Future Improvements
This project is a basic implementation, and there are several areas for potential improvement:

- Task Class: Introduce a Task class within core.py to encapsulate task-related logic.

- Error Handling: Enhance error handling with more informative messages for users.

- Structured File Format: Use a more structured file format (JSON, CSV) for task storage.

- Separation of Concerns: Further separate GUI-related code for cleaner organization.

- Enhanced Documentation: Provide additional documentation and comments for improved code understanding.

# Contributing
Contributions are welcome! Fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss the proposed changes.

# Author
[Bamidele Michael Ipadeola]-(https://github.com/ObamtechNetworks)

# Acknowledgments
This project is developed in fulfillment of the Python Internship Program by CODSOFT.
