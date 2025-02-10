from functions import add_task, delete_task, view_tasks

# Prints out the options to perform to user
def display_menu():
    print(1, "to add task")
    print(2, "to view task")
    print(3, "to delete task from list.")
    print(4, "to exit")
    print("\n")

tasks = []

while True:
    # Calls the display menu function
    display_menu()
    # Check user's input to make sure it's a numeric value, else raise Valuerror message to user
    try:
        task_choice = int(input("Enter your choice: "))
        if task_choice == 1:
            task_title = input("Enter task to add to list: ")
            add_task(tasks, task_title)
        elif task_choice == 2:
            view_tasks(tasks)
        elif task_choice == 3:
            delete_task(tasks)
        elif task_choice == 4:
            print("Bye!")
            break
        else:
            print("Invalid input!")
    except ValueError:
        print("Only numbers are allowed between 1 to 3")