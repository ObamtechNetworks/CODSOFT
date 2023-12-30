#!/usr/bin/python3
"""the main entry point for the program"""

from core import TodoAppCore
from cli import TodoAppCLI
from gui import TodoAppGUI


if __name__ == "__main__":
    app_core = TodoAppCore()
    
    while True:
        # Run either CLI or GUI based on user choice
        user_choice = input("Choose an option (cli/gui): ").lower()
        if user_choice == 'cli':
            app_cli = TodoAppCLI(app_core)
            app_cli.run()
            break
        elif user_choice == 'gui':
            app_gui = TodoAppGUI(app_core)
            app_gui.run()
            break
        else:
            print("Invalid choice. Please choose either 'cli' or 'gui'.")
