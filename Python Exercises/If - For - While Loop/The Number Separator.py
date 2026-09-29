all_numbers = []
evens = []
odds = []
while True:
    user_input = input("Enter Your Number: ").strip()
    if user_input != "stop":
        all_numbers.append(int(user_input))
        print("Number Added!")
    else:
        break
for number in all_numbers:
    if number % 2 == 0:
        evens.append(int(number))
    else:
        odds.append(int(number))
evens.sort()
odds.sort()
print(f"Even Numbers Are : {evens}")
print(f"Odds Numbers Are : {odds}")
