class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    @property
    def get_salary(self):
        return f"Your Current Salary is: {self.__salary}"
    def set_salary(self, new_salary):
        if new_salary <= 3000:
            return "Invalid Salary Amount"
        else:
            self.__salary = new_salary
            return "Salary Updated!"

my_employee = Employee("Esam", 5000)
print(my_employee.get_salary)
print(my_employee.set_salary(3000))
print(my_employee.set_salary(4000))
print(my_employee.get_salary)
