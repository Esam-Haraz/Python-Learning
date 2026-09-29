usernames = []
accepted_users = []
rejected_count = 0
while True:
    user_input = input("Enter Your Username: ").strip()
    if user_input != "end":
        usernames.append(user_input)
        print("Username Added!")
    else:
        break
for name in usernames:
    if name.startswith("A") and len(name) > 4:
        accepted_users.append(name)
    else:
        rejected_count += 1
print(f"Accepted Users: {accepted_users}")
print(f"Total Rejected: {rejected_count}")
