multiples = []
for x in range(1, 11):
    multiples.append(x * 7)
print("Multiples of 7 from 1 to 10:", multiples)

multiples = [x * 7 for x in range(1, 11)]
print("Multiples of 7 from 1 to 10 using list comprehension:", multiples)