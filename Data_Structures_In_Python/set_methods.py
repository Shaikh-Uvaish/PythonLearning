s = {3, 22, 43, 2}
print(s)
s.add(5)  # Adds the element 5 to the set anywhere.
print(s)

s.remove(2)  # Removes the element 2 from the set.
print(s)

s.discard(4583)  # Removes the element 4583 from the set if it exists.

a = {1, 2, 3}
b = {3, 4, 5}

c = a.union(b)  # Returns a new set containing all unique elements from both sets.
print(c)
d = a.intersection(b)  # Returns a new set containing only the elements that are present in both sets.
print(d)
e = a.difference(b)  # Returns a new set containing elements that are in set a but not in set b.
print(e)
f = a.symmetric_difference(b)  # Returns a new set containing elements that are in either set a or set b but not in both.
print(f)
g = a.issubset(b)  # Returns True if all elements of set a are in set b, otherwise False.
print(g)
h = a.issuperset(b)  # Returns True if all elements of set b are in set a, otherwise False.
print(h)