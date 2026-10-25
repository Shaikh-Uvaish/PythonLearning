marks = [5, 2, 21, 5, 7]
extra_marks = [35, 15, 20]

print(marks)
marks.append(10)  # adds 10 to the end of the list
print(marks)
marks.pop()  # removes the last element of the list
print(marks)
marks.insert(1, 7)  # inserts 7 at index 1
print(marks)
marks.extend(extra_marks)  # adds the elements of extra_marks to the end of marks
print(marks)