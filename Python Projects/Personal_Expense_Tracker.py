import os
base_path = os.getenv("LocalAppData")
folder_path = os.path.join(base_path, "PersonalExpenseTracker")
os.makedirs(folder_path, exist_ok=True)
file_path = os.path.join(folder_path, "ExpenseTracker.txt")

class Tracker:
    def addexpenses(self):
        category = input("Enter Your Expense Category: \n").capitalize().strip()
        if category.isalpha():
            print(f"Your Category '{category}' Has Been Added!")
        else:
            print("Alphabet Only")
            return
        amount = input("Enter Your Expense Amount: \n").strip()
        if amount.isdecimal() or amount.isdigit():
            print(f"Your Amount '{amount}' Has Been Added!")
        else:
            print("Numbers Only")
            return
        date = input("Enter Your Expense Date: \n").strip()
        print(f"Your Date '{date}' Has Been Added!")
        content = f"Category: {category}, Amount: {amount}, Date: {date}\n"
        with open(file_path, "a") as f:
            f.write(content)
    def showexpenses(self):
        with open(file_path, "r") as f:
            print("Your Expenses")
            for line in f:
                print(line.strip())

class_expenses = Tracker()

while True:
    print("__Welcome__")
    print("1. Add Expenses")
    print("2. Show Expenses")
    print("3. Quit")

    user_input = input("Enter Your Choose (1,2,3): \n").strip()
    if user_input == "1":
        class_expenses.addexpenses()
    elif user_input == "2":
        class_expenses.showexpenses()
    elif user_input == "3":
        print("GoodBye!")
        break