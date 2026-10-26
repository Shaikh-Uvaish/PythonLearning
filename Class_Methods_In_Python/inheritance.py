class Animal:
    area = "Galli"
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Generic animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Bhaao Bhaao")

class Cat(Animal):
    def speak(self):
        print("Meeow")

# a = Animal("Dogesh")
# a.speak()

d = Dog("Dogesh")
d.speak()
print(d.area)