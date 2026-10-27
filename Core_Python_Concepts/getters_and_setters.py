class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def first_name(self):
        l = self.name.split(" ")
        # print(l)
        return l[0]
    def set_first_name(self, first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name
        
e = Employee("Heera Thakur", 63453)
# e.projects = 6
# print(e.projects)

print(e.first_name())
e.set_first_name("BhanuPratap")
print(e.name)