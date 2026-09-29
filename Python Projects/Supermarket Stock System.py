import os
base_path = os.getenv("LocalAppData")
folder_path = os.path.join(base_path, "Esam The Programmer")
os.makedirs(folder_path, exist_ok=True)
file_path = os.path.join(folder_path, "stock.txt")

def add_product():
    product_name = input("Enter Your Product Name: ").strip().lower()
    if product_name.replace(" ", "").isalpha():
        print("Product Name Added")
    else:
        print("Names Only!")
        return
    product_price = input("Enter Your Product Price: ").strip()
    if product_price.isdigit():
        print("Product Price Added")
    else:
        print("Numbers Only!")
        return
    product_quantity = input("Enter Your Product Quantity: ").strip()
    if product_quantity.isdigit():
        print("Product Quantity Added")
    else:
        print("Numbers Only!")
        return
    
    with open(file_path, "a") as f:
        f.write(product_name + ":" + product_price + ":" + product_quantity + "\n")

def view_stock():
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            products = f.readlines()
            counter = 1
            for product in products:
                print(f"{counter}. {product.title()}")
                counter += 1
    else:
        print("There Is No Stock Yet!")

def update_stock():
    if os.path.exists(file_path): # بيتأكد لو الملف موجود
        print("Your Current Stock is:") # بيطبع الاستوك الحالي عن طريق انه يعمل استدعاء للدالة
        view_stock()
        wanted_stock = input("Which Stock Do You Want To Update (Product Name): ").strip().lower() # user input عشان تختار انهي منتج
        with open(file_path, "r") as f: # بتفتح الملف في وضع القراءة الاول
            updated_list = [] # فاضية مؤقتًا
            lines = f.readlines()   # عشان تفضي السطور كلها في valuble 
            found = False   # flag
            for line in lines:  # لوب على كل سطر من الvaluble
                parts = line.strip().split(":") # كل سطر بتعينه لجزء وبتقسم
                name = parts[0] # اسم المنتج هو الجزء الاول من parts
                if name.lower() == wanted_stock: # لو اسم المنتج بيساوي اللى اليوزر دخله
                    print(f"Current Quantity: {parts[2]}") # يطبع العدد الموجود حاليا
                    new_quantity = input("Enter New Quantity: ").strip() # يدخل العدد الجديد
                    parts[2] = new_quantity # بتعدل على العدد القديم بالجديد
                    new_line = ":".join(parts) + "\n" # بيعمل سطر جديد بعد ما عدلت العدد القديم بالجديد
                    updated_list.append(new_line) # ادخل السطر الجديد بالعدد الجديد لليست الفاضي
                    found = True # flag
                    print("Quantity Updated!")
                else:
                    updated_list.append(line)
            if found:
                with open(file_path, "w") as f:
                        f.writelines(updated_list) # ادخل بقا الليست للملف بعد ما عدلت على القيم اللى انا عايزها
            else:
                print("Product Not Found!")
    else:
        print("There Is No Stock Yet!")

while True:
    print("____Welcome____")
    print("1. Add Product")
    print("2. View Stock")
    print("3. Update Stock")
    print("4. Quit")
    user_input = input("Enter Your Choose: ").strip()
    if user_input == "1":
        add_product()
    elif user_input == "2":
        view_stock()
    elif user_input == "3":
        update_stock()
    else:
        print("GoodBye!")
        break
