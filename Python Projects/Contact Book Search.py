import os
base_path = os.getenv("localappdata")
folder_path = os.path.join(base_path, "Esam The Programmer")
os.makedirs(folder_path, exist_ok=True)
file_path = os.path.join(folder_path, "contacts.txt")

def add_contacts():
    contact_name = input("Enter Your Contact Name: ").strip().lower()
    if contact_name.replace(" ", "").isalpha():
        print("Contact Name Saved!")
    else:
        print("Names Only!")
        return
    contact_phone = input("Enter Your Contact Phone: ").strip()
    if contact_phone.isdigit():
        print("Contact Phone Saved!")
    else:
        print("Numbers Only!")
        return
    contact_email = input("Enter Your Contact Email: ").strip()
    if "@" in contact_email and "." in contact_email:
        print("Email Saved!")
    else:
        print("Invalid Email!")
        return
    with open(file_path, "a") as f:
        f.write(f"Name: {contact_name.title()}, Phone: {contact_phone}, Email: {contact_email.lower()}" + "\n")

def view_contacts():
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            for line in f:
                print(line.strip())
    else:
        print("File Not Found!")
        return

def contact_search():
    if os.path.exists(file_path):
        wanted_contact = input("Enter Your Contact Name To Search For: ").strip().lower()
        with open(file_path, "r") as f:
            found = False
            for line in f:
                parts = line.strip().split(",")
                contactname = parts[0].strip().split(":")
                if wanted_contact == contactname[1].strip().lower():
                    print(f"Your Contact Information is: {line.strip()}")
                    found = True
                    break
            if not found:
                print("Contact Not Found")
    else:
        print("File Not Found!")
        return

while True:
    print("___Welcome___")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search For Contact")
    print("4. Quit")
    user_input = input("Enter Your Choose: ").strip()
    if user_input.isdigit():
        if user_input == "1":
            add_contacts()
        elif user_input == "2":
            view_contacts()
        elif user_input == "3":
            contact_search()
        else:
            print("GoodBye!")
            break
    else:
        print("Enter The Number Of Your Choose!")
