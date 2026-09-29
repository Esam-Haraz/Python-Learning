class Employee:
    company_employees = []
    def __init__(self, employee_name):
        self.name = employee_name
        Employee.company_employees.append(self.name)
    @classmethod
    def show_all_employees(cls):
        return cls.company_employees

emp1 = Employee("Esam")
emp2 = Employee("Ahmed")
emp3 = Employee("Nour")
print(Employee.show_all_employees())
