grades = []
total_sum = 0
fail_count = 0
while True:
    user_input = input("Enter The Grades: ")
    if user_input != "end":
        grades.append(int(user_input))
        print("Grade Added!")
    else:
        break
for grade in grades:
    total_sum += grade
    if grade < 50:
        fail_count += 1
print(f"Class Average {total_sum / len(grades)}")
print(f"Number of Failed Students: {fail_count}")
