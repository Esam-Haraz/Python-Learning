import os
base_path = os.getenv("LocalAppData")
folder_path = os.path.join(base_path, "Esam The Programmer")
os.makedirs(folder_path, exist_ok=True)
file_path = os.path.join(folder_path, "Simple Expense Tracker.txt")

while True:
    print("__Welcome__")
    print("1. Add New Expense: ")
    print("2. Calculate Total: ")
    print("3. Quit")
    user_input = input("Enter Your Choose: ").strip()
    if user_input == "1":
        with open(file_path, "a") as f:
            item_name = input("Enter Your Item Name: ").strip()
            if item_name.replace(" ", "").isalpha():
                print("Item Added!")
            else:
                print("Name Only!")
                continue
            item_price = input("Enter Your Item Price: ").strip()
            if item_price.isdigit():
                f.write(item_name + "," + item_price + "\n")
                print("Price Added!")
            else:
                print("Number Only!")
                continue
    elif user_input == "2":
        if os.path.exists(file_path):
            total_expenses = 0
            with open(file_path, "r") as f:
                for line in f:
                    parts = line.split(",")
                    price_only = float(parts[1].strip())
                    total_expenses += price_only
            print(f"Your Total Expenses: {total_expenses}")
        else:
            print("No expenses recorded yet.")
    else:
        print("GoodBye!")
        break
