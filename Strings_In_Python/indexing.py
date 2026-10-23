name = "Shaikh Uvaish"
print(name)
#Indexing means position of letter in a string.
#Note: Indexing always starts with 0 meanwhile Length of string starts with 1.
print(name[0]) #prints first letter of string
print(name[5]) #prints sixth letter of string
#index is always n-1 where n is the length of string.
for i in range(len(name)):
    print(name[i]) #prints all letters of string one by one

#This is way to print one character at a time of a string passed.
print(name[-1]) #prints last letter of string