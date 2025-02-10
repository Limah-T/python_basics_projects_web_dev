def add_task(tasks, task_title):
    """This function expects tasks datatype as list, then append task_title recieved 
    from user's input"""
    task_title = task_title.capitalize().strip()
    if task_title in tasks:
        print(f"{task_title} is already in list!")
        return False
    tasks.append(task_title)
    print(f"{task_title} has been added to list successfully.")
    return True

def delete_task(tasks):
    """Checks if task is not empty and if task_title recieved from user is in the list, then 
    it remove the task_title, else it print message to user of task not found"""
    if not tasks:
        print("Task list is empty!")
        return False
        
    task_title = input("Enter task to delete from list: ").strip().capitalize()
    if task_title in tasks:
        tasks.remove(task_title)
        print(f"{task_title} has been removed from list successfully.")
        return True
    else:
        print(f"{task_title} not found in the list!")

def view_tasks(tasks):
    """Checks if tasks is not empty, then print all tasks prresent in the list, else print
    a message to the user"""
    if not tasks:
        print("Task list is empty!")
        return False
    for x, each_task in enumerate(tasks, start=1):
        print(f"{x}. {each_task}")
    print(f"({len(tasks)}) tasks in list")
    return True

