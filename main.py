#################################################
#   Task     : 2                                #
#   Date     : 22/10/2024                       #
#################################################

from menu import *  # Importing functions from the menu module
from time import sleep  # Importing the sleep function from the time module

# ASCII art logo
logo = """
 _____          ____           _      _       _
|_   _|  ___   |  _ \   ___   | |    (_) ___ | |_
  | |   / _ \  | | | | / _ \  | |    | |/ __|| __|
  | |  | (_) | | |_| || (_) | | |___ | |\__ \| |_
  |_|   \___/  |____/  \___/  |_____||_||___/ \__|
"""

try:
    # Prompt user to login and get user name and tasks
    name, tasks = menu_login(logo)
    
    # Wait for 1 second
    sleep(1)
    
    # Clear the command line interface
    clear_cli()
    
    # Main loop for displaying options
    while True:
        # Display menu options and handle user input
        view_option(tasks, name, logo)

# Handling the end of file error (Ctrl+D or Ctrl+C)
except EOFError:
    print("Thank You For Using To Do List 👋")  # Print a message when the program exits
