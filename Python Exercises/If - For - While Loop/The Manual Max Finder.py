temperatures = []
while True:
    user_input = input("Enter Your Temperatures: ").strip()
    if user_input != "end":
        temperatures.append(int(user_input))
        print("Temperature Added!")
    else:
        break
highest_temp = temperatures[0]
for temp in temperatures:
    if temp > highest_temp:
        highest_temp = temp
    else:
        pass
print(f"Highest Temperature Recorded is: {highest_temp}")
