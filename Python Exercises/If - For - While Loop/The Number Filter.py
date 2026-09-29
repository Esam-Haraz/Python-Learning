user_numbers = []
while True:
    user_input = input("Enter number or stop: ").strip()
    if user_input == "stop":
        print(f"All Your numbers is: {user_numbers}")
        break
    elif user_input.isdigit(): 
        user_numbers.append(int(user_input))
        print("Saved!")
    else:
        print("Invalid input, numbers only.")
for number in user_numbers:
    if number > 10:
        print(number)
