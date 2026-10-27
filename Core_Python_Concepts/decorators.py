#Decorator is a function that thakes a function, it creates a new function inside its body (wrapper). Then it returns that new function.
def decorator(func):
    def wrapper():
        print("Typing...")
        func()
        print("I have executed this function")
    return wrapper

@decorator
def say_hello():
    print("Hello")

# say_hello()

# f = decorator(say_hello)
# f()

