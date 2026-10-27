def is_greater_than_9(x):
    if x>9:
        return True
    else:
        return False

a = [1,3,5,67,200,4,32,56,7,886]
new = list(filter(is_greater_than_9, a))
# new = list(filter(lambda x: x>9, a))
print(new)