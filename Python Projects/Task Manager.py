import os
base_path = os.getenv("LocalAppData")
folder_path = os.path.join(base_path, "Esam The Programmer")
os.makedirs(folder_path, exist_ok=True)
file_path = os.path.join(folder_path, "Task Manager.txt")

def add_task():
    userinput_task = input("Enter Your New Task: ").strip()
    if userinput_task:
        with open(file_path, "a") as f:
            f.write(userinput_task + "\n")
        print("Task Added!")
    else:
        print("Empty Task!")

def view_task():
    if os.path.exists(file_path):
        print("--- Your Tasks ---")
        with open(file_path, "r") as f:
            lines = f.readlines()
            if len(lines) == 0:
                print("No tasks yet.")
            else:
                counter = 1
                for line in lines:
                    print(f"{counter}. {line.strip()}")
                    counter += 1
    else:
        print("There isn't saved tasks yet!")

def delete_task():
    view_task()
    userinput_number = input("Enter the number of the task to delete: ").strip()
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            lines = f.readlines()
            if int(userinput_number) - 1 in range(len(lines)):
                lines.pop(int(userinput_number) - 1)
                with open(file_path, "w") as f:
                    f.writelines(lines)
                    print("Task Deleted!")
            else:
                print("Out Of Range")
    else:
        print("There isn't saved tasks yet!")

while True:
    print("___Welcome___")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")
    user_input = input("Enter Your Choose: ").strip()
    if user_input == "1":
        add_task()
    elif user_input == "2":
        view_task()
    elif user_input == "3":
        delete_task()
    elif user_input == "4":
        print("GoodBye And Good Luck!")
        break
    else:
        print("Try Again!")
