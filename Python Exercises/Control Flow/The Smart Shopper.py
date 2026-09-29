total_amount = float(input("Enter Your Total Invoice: "))
if total_amount < 100:
    print(f"Your Final Price Is: ${total_amount}")
elif total_amount <= 500:
    print(f"Your Final Price Is: ${total_amount - (total_amount * 0.10)}")
else:
    print(f"Your Final Price Is: ${total_amount - (total_amount * 0.20)}")
