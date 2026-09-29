elements = ["Apple", "Orange", "Mango", "Kiwi", "Watermelon"]

for index, item in enumerate(elements, start=1):
    print(f"{index}. {item}")

try:
    user_choice = int(input("Enter Your Item Number: ").strip())
    
    if user_choice < 1:
        raise IndexError
    
    selected_item = elements[user_choice - 1]
    print(f"Your Selected Item is {selected_item}")

except IndexError:
    print("Item Not Found")
except ValueError:
    print("Please Enter Only Numbers")