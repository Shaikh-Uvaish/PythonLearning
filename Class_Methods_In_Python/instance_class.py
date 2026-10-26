class Employee:
    company = "Asus" #This is class attribute 

    def __init__(self, salary, name, bond, company):
        self.salary = salary  #Create an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary
    
    def get_emp_info(self):
        print(f"Name of employee is {self.name}. Salary = {self.salary}. Bond = {self.bond}")

e1 = Employee(32000, "Salman Khan", 3, "Google")
print(e1.company) #will always print instance attribute whenever present.
print(Employee.company) #This will help to always print class attribute.

#Object Introspection
'''An object introspection in python is basically a way to find all the methods that a particular object in python'''
print(dir(e1))