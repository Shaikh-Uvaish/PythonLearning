a = int(input("Enter number 1:"))
b = int(input("Enter number 2:"))

try:
    c = a/b
    print(c)
except Exception as e:
    print(e)

# finally block is always executed no matter try completely executes or not.
finally:
    print("This will always be executed")