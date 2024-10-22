from operation_tasks import *  # Importing functions from the operation_tasks module

###############################################################################
def menu_login(logo):
    """
    Log in or sign up for the To-Do List application.

    Args:
        logo (str): ASCII art logo of the application.

    Returns:
        tuple: A tuple containing the user's name and their tasks.
    """
    tasks = []
    while True:
        print(logo)
        print("\t\t   By: Ahmed Sharaf")
        print("\n\tWelcome To To-Do List Application 🫡")
        print("\tSelect Choice For This ⬇️: ")
        print("\t  1 - Log In  (Already User) 🙏")
        print("\t  2 - Sign Up (New User)     🆕")
        try:
            ch = int(input("\tEnter Your Choice: "))
            if ch in [1, 2]:
                if ch == 2:
                    # Sign up for a new user
                    name = input("\t\tEnter Your Name: ")
                    if os.path.exists(f"data/{name}.json"):
                        clear_cli()
                        print("\t\tThe User Already Exists 😊\n\t\tTry Again")
                        continue
                    else:
                        f = open(f"data/{name}.json", 'w')
                        print("\t\tSuccess Create The Profile 🤝")
                        break
                else:
                    # Log in for an existing user
                    name = input("\t\tEnter Your Name: ")
                    if os.path.exists(f"data/{name}.json"):
                        print("\t\tSuccess Loaded Your Profile 😊")
                        tasks = read_json(f"data/{name}.json")
                        break
                    else:
                        clear_cli()
                        print(f"\t\tThe User {name} Not Found ❌\n\t\tTry Again")
                        continue
            else:
                raise ValueError
            break
        except ValueError:
            print("\t  Enter (1 or 2 ) ")
    return name, tasks


def show(name, logo):
    """
    Display the main menu options.

    Args:
        name (str): Name of the user.
        logo (str): ASCII art logo of the application.

    Returns:
        None
    """
    print(logo)
    print(f"\t\tWelcome Ms {name.capitalize()} ❤️‍🩹")
    print(f"\t\tPlease Select Choice: ⬇️")
    print("\t\t  1 - View Tasks          📖")
    print("\t\t  2 - Add Task            ➕")
    print("\t\t  3 - Complete Task       ✔️")
    print("\t\t  4 - Show Completed Task ✔️")
    print("\t\t  5 - Delete Task         ❌")
    print("\t\t  6 - View Priority Tasks 🥇")
    print("\t\t  7 - View Due Date Tasks 📅")
    print("\t\t  8 - Details Of Task     ℹ️")
    print("\t\t  9 - Exit                👋")


def view_option(tasks, name, logo):
    """
    Display menu options and handle user input.

    Args:
        tasks (list): List of tasks, each task represented as a list.
        name (str): Name of the user.
        logo (str): ASCII art logo of the application.

    Returns:
        None
    """
    show(name, logo)
    while True:
        try:
            ch = int(input("Enter Your Choice: "))
            if ch == 1:
                view_task(tasks, name)
            elif ch == 2:
                add_task(tasks, name)
            elif ch == 3:
                if len(tasks) == 0:
                    print("\tNo Tasks To Complete. Please Add Tasks.")
                else:
                    view_task(tasks, name)
                    pos = get_pos(tasks)
                    if tasks[pos - 1][-3] == 'Yes':
                        print("This Task Is Already Completed.")
                        clear_cli()
                        show(name, logo)
                        continue
                    complete_task(pos - 1, tasks, name)
            elif ch == 4:
                comp, not_comp = split_complete(tasks, name)
                view_task(comp, name)
            elif ch == 5:
                if len(tasks) == 0:
                    print("\tNo Tasks To Delete. Please Add Tasks.")
                else:
                    view_task(tasks, name)
                    pos = get_pos(tasks)
                    delete_task(pos, tasks, name)
            elif ch == 6:
                comp, not_comp = split_complete(tasks, name)
                sort_priority(not_comp, name)
            elif ch == 7:
                comp, not_comp = split_complete(tasks, name)
                sort_date(tasks, name)
            elif ch == 8:
                details(tasks, name)
            elif ch == 9:
                print("Thank You For Using To-Do List 👋")
                exit()
            else:
                raise ValueError
            break
        except ValueError:
            print("Enter A Number Between 1 and 9 🙄")
