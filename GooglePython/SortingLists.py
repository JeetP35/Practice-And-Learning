#Lesson 1

numbers = [5,6,7,3,2,45,4,23,12,34,22]
numbers.sort()
#Output the sorted list
print(numbers)

names=["John","Alice","Bob","Diana","Charlie"]
#Output the list before and after sorting
print("Before sorting:", names)
names.sort()
print("After sorting:", names)
#Another way of sorting without changing the original list
print(sorted(names))

#Output in length order
names.sort(key=len)
print("Sorted by length:", names)
#OR another way doing the same thing
print(sorted(names, key=len))