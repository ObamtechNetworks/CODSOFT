# TODO List App

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
![TODO APP GUI](https://postimg.cc/7551N69G)

### enter task
![ENTER TASK](https://postimg.cc/gnkHn46K)

### select task
![ENTER TASK](https://postimg.cc/Yhnfgg6B)

### mark task completed
![MARK TASK COMPLETED](https://postimg.cc/XXnwzxx0)

### remove unfinished task
![REMOVE UNFINISHED TASK](https://postimg.cc/8j0MsGG1)

### remove completed task
![REMOVE COMPLETED TASK](https://postimg.cc/qN6n3FB2)

### GUI created tasks persists
![CREATED TASK PERSISTS GUI](https://postimg.cc/zbrn5krK)

# CLI Version
- Open a terminal.
- Navigate to the project directory.

- Run the following command:

```bash
python3 main.py
```

## TODO LIST CLI SCREENSHOTS
### main window
![TODO APP CLI](https://postimg.cc/67RdDmDB)

### add task
![ADD TASK](https://postimg.cc/5XDBKVKP)

### ongoing task
![ONGOING TASK](https://postimg.cc/QHtcXtR4)

### mark task completed
![MARK TASK COMPLETED](https://postimg.cc/pykDb815)

### completed task
![MORE TASK](https://postimg.cc/SYQCYNjK)

### remove completed task
![EXIT](https://postimg.cc/vgt5m6Yj)

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
