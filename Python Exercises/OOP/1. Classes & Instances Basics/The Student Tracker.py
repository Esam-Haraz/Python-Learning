class Student:
    def __init__(self, student_name):
        self.student = student_name
        self.grades = {}
    def add_grade(self, grade_key, grade_value):
        self.grades[grade_key] = grade_value   # To Add Items Into A Dictionary
        return f"{grade_key} Added With {grade_value}"
    def get_average(self):
        total_sum = sum(self.grades.values())
        subject_count = len(self.grades.values())
        average = total_sum / subject_count
        return f"{self.student}'s Average Grade Is: {average}"

student_data = Student("Esam")
print(student_data.add_grade("Arabic", 100))
print(student_data.add_grade("Math", 85))
print(student_data.get_average())
