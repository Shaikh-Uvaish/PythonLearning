#Strings Formatting

description = "However, {} is a Great {} Player"
a = "Ronaldo"
a1 = "Football"
b = "Dhoni"
b1 = "Cricket"
d = "Gukesh"
d1 = "Chess"

# .format() method is used formatting in python.

# s1 = description.format(a, a1)
# print(s1)
# s2 = description.format(b, b1)
# print(s2)
# s3 = description.format(d, d1)
# print(s3)

#To enhance this logic developers of python came up with idea of making fstrings.
#Which was later adapted as a best way of write a logic.
print(f"However, {a} is a Great {a1} Player")
print(f"However, {b} is a Great {b1} Player")
print(f"However, {d} is a Great {d1} Player")

#However, fstrings are mostly used in python instead of .format() due to it's readability and understandings
