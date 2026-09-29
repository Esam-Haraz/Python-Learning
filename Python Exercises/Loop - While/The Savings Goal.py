goal = int(input("Enter Your Goal: "))
saved_amount = 0
while saved_amount < goal:
    saved_amount += int(input("Deposit Amount: "))
    print(f"Current Saving: {saved_amount}")
else:
    print(f"Goal Reached! Total: {saved_amount}")
