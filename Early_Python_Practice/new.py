def selection_sort(salaries):
n=len(salaries)
for i in range(n):
min_index=i
for j in range(i+1,n):
if salaries[j]<salaries[min_index]:
min_index=j
salaries[i],salaries[min_index]=salaries[min_index],salaries[i]
return salaries
def bubble_sort(salaries):
n=len(salaries)
for i in range(n):
for j in range(0,n-i-1):
if salaries[j]>salaries[j+1]:
salaries[j] , salaries[j+1]=salaries[j+1],salaries[j]
return salaries
salaries=[50000.0,72000.5,48000.75,91000.2,61000.0,87000.5,76000.4,52000.3,95000.0,69000.7]
print("selection sort:")
sorted_salaries_selection=selection_sort(salaries.copy())
print("sorted salaries:",sorted_salaries_selection)
print("Top 5 salaries:",sorted_salaries_selection[-5:][::-
1])
print("\nBubble sort:")
sorted_salaries_bubble=bubble_sort(salaries.copy())
print("sorted salaries:",sorted_salaries_bubble)
print("Top 5 salaries:",sorted_salaries_bubble[-5:][::-1])