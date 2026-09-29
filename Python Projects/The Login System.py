import os
base_path = os.getenv("LocalAppData")
folder_path = os.path.join(base_path, "Esam The Programmer")
os.makedirs(folder_path, exist_ok=True)
file_path = os.path.join(folder_path, "Login System.txt")

while True:
    print("Welcome")
    print("1. Register")
    print("2. Login")
    print("3. Quit")
    user_input = input("Enter Your Choose: ").strip()
    if user_input == "1":
        input_user = input("Enter Your Username: ").strip()
        input_pass = input("Enter Your Password: ").strip()
        print("Your User Registered Successfully")
        with open(file_path, "a") as f:
            f.write(input_user + "," + input_pass + "\n")
    elif user_input == "2":
        login_user = input("Enter Your Username: ").strip()
        login_pass = input("Enter Your Password: ").strip()
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                is_found = False
                for line in f:
                    parts = line.split(",")
                    saved_user = parts[0].strip()
                    saved_pass = parts[1].strip()
                    if login_user == saved_user and login_pass == saved_pass:
                        print(f"Login Successfull! Welcome {login_user}")
                        is_found = True
                        break
                if is_found == False:
                    print("Wrong Username Or Password")
        else:
            print("There is no Saved Data!")
    else:
        break
