import os
base_path = os.getenv("LocalAppData")
folder_path = os.path.join(base_path, "Esam The Programmer")
os.makedirs(folder_path, exist_ok=True)
file_path = os.path.join(folder_path, "The Guest Book.txt")

while True:
    print("--- Welcome To The Guest Book ---")
    print("1. Sign Guest Book")
    print("2. View Guests")
    print("3. Quit")
    user_choice = input("Choose: ").strip().lower()
    if user_choice == "1":
        with open(file_path, "a") as f:
            user_name = input("Enter Your Name: ").strip()
            if user_name.replace(" ", "").isalpha() == True:
                f.write(user_name.title() + "\n")
                print("Name Added!")
            else:
                print("Names Only")
    elif user_choice == "2":
        if os.path.exists(file_path):
            print("--- Guests List ---")
            with open(file_path, "r") as f:
                print(f"{f.read()}")
            print("------------------")
        else:
            print("\n[!] No Guests Have Signed Yet.")
    else:
        break

