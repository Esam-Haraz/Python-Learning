passwords = []
upper_count = 0
lower_count = 0
digit_count = 0

while True:
    user_input = input("Enter Your Password: ").strip()
    if user_input != "done":
        passwords.append(user_input)
        print("Password Added!")
    else:
        break
for password in passwords:
    for Pass in password:
        if Pass.isupper():
            upper_count += 1
        if Pass.islower():
            lower_count += 1
        if Pass.isdigit():
            digit_count += 1

print(f"Capital Letters: {upper_count}")
print(f"Small Letters : {lower_count}")
print(f"Digits: {digit_count}")
