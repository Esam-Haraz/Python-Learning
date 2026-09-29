def check_grades(marks_list):
    for mark in marks_list:
        if mark >= 50:
            print(f"Your Score is: {mark}, and you have passed!")
        else:
            print(f"Your Score is: {mark}, and you did not pass")

class_a_scores = [90, 45, 50, 88, 33]
check_grades(class_a_scores)
