try:
    user_age = int(input("Enter Your Age: ").strip())
    if user_age < 0:
        raise TypeError("Age cannot be negative") # this is the terminal error explaniation not print command
    print("Valid Age")
except ValueError:
    print("Only Numbers")
except TypeError:
    print("Are You Kidding me!!")
