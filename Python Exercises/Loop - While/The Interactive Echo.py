user_word = input("Enter Your Word: ")
while user_word.strip().lower() != "exit":
    print(f"{user_word}")
    user_word = input("Enter Your Word: ")
else:
    print("Program Closed")
