employees = {"Esam": 5000, "Ahmed": 8000, "Waleed": 7000}
user_employee_name = input("Enter Your Name: ").strip().title()
try:
    salary = employees[user_employee_name]
    print(f"Your Salary is {salary}")
    
except KeyError:
    print("Employee not found in our records.")