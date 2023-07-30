import time


tasks=[]

def show_menu():
    print('------------------TO DO LIST MENU----------------------------------')
    print("To-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task(tasks):
    task=input('Please type the task that you want to add')
    tasks.append(task)
    print('Adding task please wait.....')
    time.sleep(3)
    print('task added successfully!')


def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")


def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the number of the task to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' removed successfully!")
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Your to-do list is empty. Nothing to remove.")

while(True):
    show_menu()
    choice=int(input('Type the Menu task here'))
    if choice==1:
        add_task(tasks)
    elif choice==2:
        view_tasks(tasks)
    elif choice==3:
        remove_task(tasks)
    elif choice==4:
        print('Exiting the list good bye')
        break
    else:
        print('invalid instruction')