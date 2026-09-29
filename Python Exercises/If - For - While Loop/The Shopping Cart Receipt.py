prices = []
total_cost = 0
expensive_count = 0
while True:
    user_input = input("Enter The Product Price: ").strip()
    if user_input != "done":
        prices.append(int(user_input))
        print("Price Added!")
    else:
        break
for number in prices:
    total_cost += number
    if number >= 100:
        expensive_count += 1
print(f"Total Bill: {total_cost}")
print(f"Items over $100: {expensive_count}")
