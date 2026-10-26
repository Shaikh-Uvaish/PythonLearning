#Class:- Class is a blueprint or template.
#For example:- A exam form containing attributes like name, roll no., sandard, etc.

#Objet=ct:- An object is an instance of the class. 
#For example:- A student filling the exam form is an object of the class.

class Employee:
    company = "Google"  # Class variable

    def get_salary(self):
        return 42000  # Instance method

e = Employee() #This is an object of class Employee created here.
print(e.get_salary())  # Output: 42000 Employee get_slary() is called here.
print(e.company)