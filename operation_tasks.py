import copy
from helped_fun import *

##########################################################################
def view_task(tasks, name):
    """
    Display tasks for a given user.

    Args:
        tasks (list): List of tasks, each task represented as a tuple.
                      Each tuple contains task name, start date, end date,
                      completion status, priority, and details.
        name (str): Name of the user.

    Returns:
        None
    """
    # Printing the header
    print("\t" * 5, f" Your Tasks Ms {name.capitalize()} ⬇️", sep='')
    print("\t", "-" * 90, sep='')
    print("\tindex |       Task Name      | Start Date | End Date  | Complete |   Priority   | Details")
    print("\t", "-" * 90, sep='')

    count = 1  # Counter for task indexing
    # Looping through each task
    for x in tasks:
        # Determining the priority level
        if x[-2] == 3:
            p = "High  "
        elif x[-2] == 2:
            p = "Medium"
        else:
            p = "Low   "

        # Determining completion status
        if x[-3] == 'Yes':
            m = "✔️ "
        else:
            m = "❌ "

        # Printing task details
        print(f"\t{count:^5} | {x[0]:^20} | {x[1]:^10} | {x[2]:^8} |    {m}   |    {p}    | {x[5]}")
        print("\t", "-" * 90, sep='')
        count += 1

def get_pos(tasks):
    """
    Get the position of the task selected by the user.

    Args:
        tasks (list): List of tasks, each task represented as a list.

    Returns:
        int: The position of the task selected by the user.
    """
    while True:
        try:
            pos = int(input(f"\tEnter the number of the task: "))
            if pos < 1 or pos > len(tasks):
                raise ValueError
            break
        except ValueError:
            print(f"\tEnter a valid position from 1 to {len(tasks)}")
    return pos


#####################################
def add_task(tasks, name):
    """
    Add a new task to the list of tasks for a given user.

    Args:
        tasks (list): List of tasks, each task represented as a list.
                      Each task list contains task name, start date, end date,
                      completion status, priority, and details.
        name (str): Name of the user.

    Returns:
        None
    """
    # Initialize variables to store task details
    t_name, start, end, priority, note = '', '', '', '', ''
    
    # Clearing the command line interface
    clear_cli()
    
    # Getting task details from the user
    print(f"\tPlease Ms {name.capitalize()} Enter Some info About Task ❤️‍🩹")
    
    # Input task name with validation
    while True:
        t_name = input("Enter Task Name: ")
        if len(t_name) > 20:
            print("Please Enter Name Less Than 20 Characters !")
            continue
        break
    
    # Inputting start date manually or using current date
    while True:
        try:
            ch = input("Do You Need to Enter Start Date Manually? (Yes/No): ").capitalize()
            if ch not in ['Yes', 'Y', 'No', 'N']:
                raise ValueError
            break
        except ValueError:
            print("Enter Valid Option: Yes or No")

    while True:
        try:
            if ch in ['Yes', 'Y']:
                start = input("Enter Start Date ('day-month-year'): ")
                if convert_to_time(start) < dt.datetime.now().date():
                    raise ValueError
            else:
                start = dt.datetime.now().date().strftime(f"%d-%m-%Y")
            break
        except ValueError:
            print("Invalid Date. Please Try Again.")
    
    # Inputting end date with validation
    while True:
        try:
            end = input(f"Enter End Date ('Deadline') ('day-month-year'): ")
            if convert_to_time(end) < convert_to_time(start):
                raise ValueError
            break
        except ValueError:
            print("Invalid Date. Please Try Again.")

    # Inputting priority level with validation
    priority = input("Please Select Priority (High/Medium/Low): ").capitalize()
    while True:
        if priority in ['High', 'H', 'Medium', 'M', 'Low', 'L']:
            if priority in ['High', 'H']:
                priority = 3
            elif priority in ['Medium', 'M']:
                priority = 2
            else:
                priority = 1
        else:
            priority = input("Please Select Priority (High/Medium/Low): ").capitalize()
            continue
        break

    # Inputting task details
    note = input(f"Enter Some Details About Tasks: ")

    # Appending the new task to the task list
    tasks.append(list([t_name, start, end, 'No', priority, note]))
    
    # Informing the user about the successful insertion
    print(f"\t Success To Insert Task ✔️")
    
    # Viewing the updated task list
    view_task(tasks, name)
    
    # Writing the updated task list to the JSON file
    write_json(tasks, f"data/{name}.json")
#####################################
def delete_task(pos, tasks, name):
    """
    Delete a task from the list of tasks for a given user.

    Args:
        pos (int): Position of the task to be deleted in the list (1-based indexing).
        tasks (list): List of tasks, each task represented as a list.
                      Each task list contains task name, start date, end date,
                      completion status, priority, and details.
        name (str): Name of the user.

    Returns:
        None
    """
    # Deleting the task from the list based on the provided position
    del tasks[pos - 1]
    
    # Viewing the updated task list
    view_task(tasks, name)
    
    # Writing the updated task list to the JSON file
    write_json(tasks, f"data/{name}.json")


#################################################
def complete_task(idx, tasks, name):
    """
    Mark a task as complete.

    Args:
        idx (int): Index of the task to be marked as complete (0-based indexing).
        tasks (list): List of tasks, each task represented as a list.
                      Each task list contains task name, start date, end date,
                      completion status, priority, and details.
        name (str): Name of the user.

    Returns:
        None
    """
    # Marking the task at the specified index as complete
    tasks[idx][-3] = "Yes"
    
    # Viewing the updated task list
    view_task(tasks, name)


def split_complete(tasks, name):
    """
    Split tasks into complete and incomplete lists.

    Args:
        tasks (list): List of tasks, each task represented as a list.
                      Each task list contains task name, start date, end date,
                      completion status, priority, and details.
        name (str): Name of the user.

    Returns:
        tuple: A tuple containing two lists: complete tasks and incomplete tasks.
    """
    incomplete_tasks = []
    complete_tasks = []
    
    # Looping through each task and segregating them based on completion status
    for task in tasks:
        if task[-3] == 'No':
            incomplete_tasks.append(task)
        else:
            complete_tasks.append(task)
    
    return complete_tasks, incomplete_tasks

  
#################################################
def sort_priority(tasks, name):
    """
    Sort tasks by priority and display them.

    Args:
        tasks (list): List of tasks, each task represented as a list.
                      Each task list contains task name, start date, end date,
                      completion status, priority, and details.
        name (str): Name of the user.

    Returns:
        None
    """
    # Create a deep copy of the tasks list to avoid modifying the original list
    t = copy.deepcopy(tasks)
    
    # Sorting tasks by priority
    for i in range(len(t)):
        for j in range(i+1, len(t)):
            if t[i][-2] < t[j][-2]:
                t[i], t[j] = t[j], t[i]
    
    # Displaying the sorted tasks
    view_task(t, name)


def sort_date(tasks, name):
    """
    Sort tasks by start date and display them.

    Args:
        tasks (list): List of tasks, each task represented as a list.
                      Each task list contains task name, start date, end date,
                      completion status, priority, and details.
        name (str): Name of the user.

    Returns:
        None
    """
    # Create a deep copy of the tasks list to avoid modifying the original list
    t = copy.deepcopy(tasks)
    
    # Sorting tasks by start date
    for i in range(len(t)):
        for j in range(i+1, len(t)):
            x_ = convert_to_time(t[i][-4])
            y_ = convert_to_time(t[j][-4])
            if x_ > y_:
                t[i], t[j] = t[j], t[i]
    
    # Displaying the sorted tasks
    view_task(t, name)

##################################################
def details(tasks, name):
    """
    Display task details for a given user.

    Args:
        tasks (list): List of tasks, each task represented as a list.
                      Each task list contains task name, start date, end date,
                      completion status, priority, and details.
        name (str): Name of the user.

    Returns:
        None
    """
    # Printing the header
    print("\t" * 5, f" Your Tasks Ms {name.capitalize()} ⬇️", sep='')
    print("\t", "-" * 85, sep='') 
    print("\tindex |       Task Name      | Details")
    print("\t", "-" * 85, sep='')

    count = 1  # Counter for task indexing
    # Looping through each task
    for x in tasks:
        # Printing task details
        print(f"\t{count:^5} | {x[0]:^20} | {x[-1]}")
        print("\t", "-" * 85, sep='') 
        count += 1
