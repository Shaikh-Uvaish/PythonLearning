# Functions are like reusable piece of code that can be called multiple times
#in python every function is defined using def keyword.
def my_function():
    print("Hello from a function")
#This is the Function Definition, but it is useless until it gets called.
my_function() #This is the Function Call, which will execute the function and print the statement.

#A function accepts arguments, which are values that can be passed to the function to perform operations.
def my_function1(name):
    print(f"Hello {name} from a function")
my_function1("Alice")

def average(num1, num2, num3):
    return (num1 + num2 + num3) / 3.0
result = average(15, 22, 33)
print(result)
#return is a final statement in a function.
#As soon as the return statement is executed, the function terminates and returns the value to the caller.