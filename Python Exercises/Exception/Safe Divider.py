try:
    first_number = int(input("Enter Your First Number: ").strip())
    second_number = int(input("Enter Your Second Number: ").strip())
    result = first_number / second_number
except ValueError:
    print("Enter Only Numbers")
except ZeroDivisionError:
    print("Can't Divine By Zero")
else:
    print(f"Your Result is {result}")
