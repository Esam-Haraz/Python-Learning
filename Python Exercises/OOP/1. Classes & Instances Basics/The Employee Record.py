class Employee:
    def __init__(self, emp_name, emp_position, emp_salary):
        self.name = emp_name
        self.position = emp_position
        self.salary = emp_salary
    def get_info(self):
        return f"Your Name is: {self.name}, And Your Position is: {self.position}, And Your Salary is: {self.salary}"

employee_one = Employee("Ahmed", "Python Developer", 15000)
print(employee_one.get_info())
