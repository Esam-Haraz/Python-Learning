age = int(input("Enter Your Age: "))
if age < 12:
    print("Your Ticket Price Is: $5")
elif age <= 17:
    print("Your Ticket Price Is: $8")
elif age <= 60:
    print("Your Ticket Price Is: $12")
else:
    print("Your Ticket Price Is: $7")
