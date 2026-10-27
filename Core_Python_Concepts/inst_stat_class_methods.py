# instance, static, class method
class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    #This is an instance method (default)
    def print_info(self):
        info = f"the name is {self.name} and salary is {self.salary}"
        print(info)

    #static method :- it is a method that doen't needs self arg
    @staticmethod
    def sum(a, b):
        return a+b

    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

e1 = Employee("Jack", 2323)
e2 = Employee("Jill", 2654)
# print(Employee.company)
# e1.print_info()
# e2.print_info()
# print(e2.sum(10, 45))

e1.print_company()
e1.change_company("Google")
e1.print_company()
print(Employee.company)
