banned_users = ["admin", "root", "system", "hacker"]
username = input("Enter Your Username: ")
if username in banned_users:        # AI corrected me to use "in"
    print("Access Denied: This Username Is Banned")
else:
    print(f"Welcome {username}")