marks = {"John": 85, "Alice": 92, "Bob": 78}
print(marks)
print("Marks before updating")
#Instead of using index we can access the elements of dictionary using keys.
print(marks["Bob"]) #78 will be the output.
#We can also update the elements of dictionary using keys.
marks["Alice"] = 95
print("Marks after updating")
print(marks)