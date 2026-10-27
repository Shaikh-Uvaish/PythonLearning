#Here we take repeat as a function containing nested function decorator. A decorator will also accept the function func and it again contains a nested function called wrapper(). n --> is a argument that tells about how many times do we have to repeate this. a --> is an argument that we use to accept a paramater in my case "Uvaish".
def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper #this will help to return the wrapper function. that is func passed on.
    return decorator #this will help to return a decorator function.

@repeat(7)
def say_hello(a):
    print(f"Hello! {a}")

'''
It replaces the say_hello function with this:-
def decorator(func):
    def wrapper(a):
        for i in range(n):
            say_hello(a)
    return wrapper()
'''


say_hello("Uvaish")