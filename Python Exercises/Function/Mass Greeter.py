names = []
while True:
    user_input = input("Enter Your Names: ")
    if user_input != "done":
        if user_input.isalpha():
            names.append(user_input.strip().capitalize())
            print("Name Added!")
        else:
            print("Only Names!")
    else:
        break
def say_hello(*people):
    for name in people:
        print(f"Hello {name}")
say_hello(*names)
