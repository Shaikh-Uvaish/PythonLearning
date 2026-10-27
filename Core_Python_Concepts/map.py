#Higher-order functions in python are
# map, filter and reduce
#They operates on iterables

numbers = [1, 2, 3, 4, 5]

# def square(a):
#     return a * a

# new = list(map(square, numbers))
new = list(map(lambda x: x*x, numbers))
print(new)