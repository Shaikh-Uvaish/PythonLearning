class Employee:
    def __init__(self, salary, name, age):
        self.salary = salary  #Create an instance attribute of name salary and assign it with salary
        self.name = name
        self.age = age

    def get_salary(self):
        return self.salary
    
    def get_emp_info(self):
        print(f"Name of employee is {self.name}. Salary = {self.salary}")

e1 = Employee(42000, "Uvaish", 30)
print(e1.get_salary())  # Output: 42000
e1.get_emp_info()