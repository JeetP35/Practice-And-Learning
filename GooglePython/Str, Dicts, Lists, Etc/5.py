x = ["apple", "banana", "cherry"]
print("Type of x:", type(x))
print("length :", len(x))
print("First element:", x[0])
print("Last element:", x[-1])
print("Elements from index 1 to 2:", x[1:3])

x.append("date")
print("After appending 'date':", x)

x.insert(1, "blueberry")
print("After inserting 'blueberry' at index 1:", x)

x.remove("banana")
print("After removing 'banana':", x)

x.pop()
print("After popping last element:", x)

x.sort()
print("After sorting:", x)

x.reverse()
print("After reversing:", x)

x[-1] = "dragonfruit"
print("After changing last element to 'dragonfruit':", x)