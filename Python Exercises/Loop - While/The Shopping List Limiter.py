shopping_list = []
while len(shopping_list) < 5:
    shopping_list.append(input("Enter Your Item: ").strip())
    print(f"Item Added, and the current items count is: {len(shopping_list)}")
else:
    print(shopping_list)
    print("The list is full")
