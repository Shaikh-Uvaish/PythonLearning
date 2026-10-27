def sum(*args):
    # print(args)
    # args is list like 
    total = 0
    for item in args:
        total += item
    return total

print(sum(67,3,5))