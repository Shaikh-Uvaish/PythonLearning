while True:
    try:
        a = int(input("Enter number 1:"))
        b = int(input("Enter number 2:"))

        print(f"The division is {a / b}")
    except ValueError:
        print("Please dont perform bad typecast")

    except ZeroDivisionError:
        print("Can't divide integer by zero")
    except Exception as e:
        print("Unknown error occured", e)

