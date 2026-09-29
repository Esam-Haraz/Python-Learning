salaries = []
total_tax = 0 # total taxed money
while True:
    user_input = input("Enter The Salary: ")
    if user_input != "end":
        salaries.append(int(user_input))
    else:
        break
for salary in salaries:
    if salary >= 5000:
        tax = salary * 10 / 100
        total_tax += tax
    else:
        tax = salary * 5 / 100
        total_tax += tax
print(f"Total Tax Collected: {total_tax}")
