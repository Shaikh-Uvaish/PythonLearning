#recursion in python is used where function calls itself to solve a problem.
#consider an example of fibonacci series where each number is the sum of the two preceding ones.
'''
fib(0) = 0
fib(1) = 1
fib(2) = fib(0) + fib(1)
fib(3) = fib(1) + fib(2)
fib(4) = fib(2) + fib(3) .....
fib(n) = fib(n-1) + fib(n-2)
'''
def fibonacci(n):
    if(n == 0 or n ==1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))  # Output: 13