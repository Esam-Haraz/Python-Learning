import os
base_path = os.getenv("localappdata")
folder_path = os.path.join(base_path, "Esam The Programmer")
os.makedirs(folder_path, exist_ok=True)
file_path = os.path.join(folder_path, "expenses.txt")

def add_expense():
    input_date = input("Enter The Date Of Your Expense: ").strip()
    if input_date.replace(" ", "").isdigit():
        print("Date Added!")
    else:
        print("Numbers Only!")
        return
    input_category = input("Enter The Category: ").strip().lower()
    if input_category.replace(" ", "").isalpha():
        print("Category Saved!")
    else:
        print("Categories like 'Food, bills, etc' Only Are Allowed!")
        return
    input_amount = input("Enter The Amount: ").strip()
    if input_amount.replace(" ", "").isdigit():
        print("Amount Saved!")
    else:
        print("Numbers Only!")
        return
    
    with open(file_path, "a") as f:
        f.write(input_date.replace(" ", "-") + ":" + input_category + ":" + input_amount + "\n")

def view_expense():
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            print("_____Your Expenses Are_____")
            print(f.read())
    else:
        print("There Is No Expenses Saved Yet!")

def calculate_total():
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            lines = f.readlines()
            total_sum = 0
            for line in lines:
                parts = line.strip().split(":")
                amounts = int(parts[2])
                total_sum += amounts
            print(f"Your Total Expenses: {total_sum}")
    else:
        print("There Is No Expenses Saved Yet!")

while True:
    print("Welcome")
    print("1. Add Expenses")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Quit")
    user_input = input("Enter Your Choose: ").strip()
    if user_input == "1":
        add_expense()
    elif user_input == "2":
        view_expense()
    elif user_input == "3":
        calculate_total()
    else:
        print("GoodBye!")
        break
