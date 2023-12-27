# Password Generator

This password generator is a Python program developed by Bamidele Michael Ipadeola. It was created as part of the tasks given by CODSOFT company for the Python programming internship.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Modules](#modules)
  - [Main Module (Entry)](#main-module-entry)
  - [Password Generator Module](#password-generator-module)
  - [Utilities Module](#utilities-module)
  - [Character Lists Module](#character-lists-module)
- [How to Use](#how-to-use)
  - [Getting Started](#getting-started)
  - [Running the Password Generator](#running-the-password-generator)
  - [Input Validation](#input-validation)
  - [Exception Handling](#exception-handling)
  - [File Operations](#file-operations)
  - [Logging](#logging)
- [Contributor](#contributor)
- [License](#license)

## Introduction

This password generator is a simple yet robust tool developed in Python. It allows users to create secure passwords with a customizable combination of letters, symbols, and digits. The program provides an intuitive interface for users to specify their password requirements and optionally save the generated password to a file with a timestamp.

## Features

- Customizable password length, symbols, letters, and digits.
- Timestamping of generated passwords.
- Option to reveal or hide the generated password.
- Automatic saving of passwords to a text file.
- Logging of errors for debugging and monitoring.

## Modules

### Main Module (Entry)

- **File:** `main.py`
- **Description:** Entry point for the password generator application. Displays a welcome message, collects user input, and invokes the password generation process.

### Password Generator Module

- **File:** `passwd_gen.py`
- **Description:** Defines the `passwd_machine` function, which collects user input for password specifications, generates the password, handles user interactions, and saves the password to a file.

### Utilities Module

- **File:** `utils.py`
- **Description:** Contains utility functions used throughout the program, including input validation, random character generation, screen clearing, and program exit handling.

### Character Lists Module

- **File:** `character_lists.py`
- **Description:** Provides lists of characters (letters, digits, symbols) used by the password generator.

## How to Use

### Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/password-generator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd password-generator
    ```

### Running the Password Generator

Execute the following command to run the password generator:

```bash
python3 main.py
```

Follow the on-screen prompts to specify password requirements and generate a password.

# Input Validation
The program validates user inputs to ensure they are valid positive integers. If an invalid input is detected, an error message is displayed, and the user is prompted to enter a valid value.

# Exception Handling
The program includes robust exception handling to gracefully handle errors during password generation, file operations, and user input.

# File Operations
Generated passwords are automatically saved to a text file named passwd.txt along with a timestamp. If there are any issues with file operations, error messages are displayed, and the program continues execution.

# Logging
Error messages and exceptions are logged to a file named `password_generator.log`. This log file provides valuable information for debugging and monitoring the behavior of the application.

# Developer
Bamidele Michael Ipadeola
