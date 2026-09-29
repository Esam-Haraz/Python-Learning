import os
base_path = os.getenv("localappdata")
folder_path = os.path.join(base_path, "Esam The Programmer")
os.makedirs(folder_path, exist_ok=True)
file_path = os.path.join(folder_path, "Contact Book.txt")

def add_contact():
    input_name = input("Enter Your Contact Name: ").strip().lower()
    if input_name.replace(" ", "").isalpha():
        print("Name Added!")
    else:
        print("Names Only!")
        return
    input_phone = input("Enter Your Contact Phone: ").strip()
    if input_phone.isdigit() and len(input_phone) >= 11:
        print("Number Added!")
    else:
        print("Numbers Only!")
        return
    with open(file_path, "a") as f:
        f.write(input_name.title() + "," + input_phone + "\n")
    print("Contact Saved!")

def view_contact():
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            print(f"Your Current Saved Contacts: \n{f.read()}")
    else:
        print("No Contacts Saved Yet!")

while True:
    print("___Welcome___")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Quit")
    user_input = input("Enter Your Choose: ").strip()
    if user_input == "1":
        add_contact()
    elif user_input == "2":
        view_contact()
    else:
        print("GoodBye")
        break
