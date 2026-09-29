database = []
target = 0
count = 0
while True:
    user_input = input("Enter Your Numbers: ").strip()
    if user_input == "done":
        break
    if user_input.isdigit():
        database.append(int(user_input))
        print("Number Added!")
    else:
        print("Number Only")
target = int(input("Enter the number you want to search for: "))
for num in database:
    if num == target:
        count += 1
print(f"Number {target} Was Found {count} Times")
