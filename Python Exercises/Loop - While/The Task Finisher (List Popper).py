tasks = ["Study Python", "Workout", "Read Book", "Sleep"]
while len(tasks) > 0:
    current_task = tasks.pop()
    print(f"Completed: {current_task}")
    print(f"Tasks Remaining: {len(tasks)}")
else:
    print("All Tasks Done, Good Job")

print("#" * 50) # Seperator

tasks1 = []
slots = int(input("Enter How much Tasks do you have for today \"Numbers Only\":"))
while len(tasks1) < slots:
    tasks1.append(input("Enter Your Tasks for Today: ").strip().lower())
    print(f"Task Added! Your Remaining Free Slots is: {slots - 1}")
else:
    current_task1 = input("Which Task did you complete: ").strip().lower()
    tasks1.remove(current_task1)
    print(f"Remaining Tasks are: {tasks1}")

tasks = []
slots = int(input("How many tasks do you have for today: "))
while len(tasks) < slots:
    new_task = input("Enter Your New Task: ").strip().lower()
    tasks.append(new_task)
    print(f"Task Added! Remaining Slots: {slots - len(tasks)}")

print("-" * 30)
print(f"Your To-Do List is ready: {tasks}")
print("-" * 30)

while len(tasks) > 0:
    current_task = input("Which Task Did You Complete?: ").strip().lower()
    if current_task in tasks:
        tasks.remove(current_task)
        print(f"Great! Task Removed. Remaining Tasks: {tasks}")
    else:
        print("Task Not Found In The List, Check Again")
else:
    print("All Tasks Done! You Are Free Now")

