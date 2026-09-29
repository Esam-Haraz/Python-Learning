import os
base_path = os.getenv("localappdata")
folder_path = os.path.join(base_path, "Esam The Programmer")
os.makedirs(folder_path, exist_ok=True)
file_path = os.path.join(folder_path, "Grade Calculator.txt")

def calculate_grade(score):
    if score >= 85:
        return "Excellent"
    elif score >= 75 and score <= 85:
        return "Very Good"
    elif score >= 65 and score <= 75:
        return "Good"
    elif score >= 50 and score <= 65:
        return "Pass"
    else:
        return "Fail"

def add_student():
    student_name = input("Enter Your Student Name: ").strip().lower()
    if not student_name.replace(" ", "").isalpha():
        print("Names Only!")
        return
    else:
        print("Name Added!")
    student_grade = input("Enter Your Student Grade: ").strip()
    if not student_grade.isdigit():
        print("Numbers Only!")
        return
    score = int(student_grade)
    if not (0 <= score <= 100):
        print("Score Must Be Between 0 and 100")
        return
    grade = calculate_grade(score)
    with open(file_path, "a") as f:
        f.write(student_name + ":" + student_grade + f"({grade})" + "\n")

def view_students():
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            print(f.read())
    else:
        print("No Record Saved Yet!")
        return

while True:
    print("___Welcome")
    print("1. Add New Student")
    print("2. View Current Students")
    print("3. Quit")
    user_input = input("Enter Your Choose: ").strip()
    if user_input == "1":
        add_student()
    elif user_input == "2":
        view_students()
    else:
        print("GoodBye!")
        break
