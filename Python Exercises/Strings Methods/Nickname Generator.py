name = input("Enter your First and Last Name: ")
names = name.split()
first_name = names[0]
last_name = names[1]
new_username = first_name[0:3] + last_name[0:3]

print(new_username.lower() + "123")
