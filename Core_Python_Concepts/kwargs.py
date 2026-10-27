def marks(**kwargs):
    # kwargs is a dictionary with all key-value pairs which were passed as marks
    for item in kwargs:
        print(f"the marks of {item} is {kwargs[item]}")

marks(shubham=45, vaibhav=75, ashish=57)