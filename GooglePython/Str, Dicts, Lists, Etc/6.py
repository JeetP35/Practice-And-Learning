tuple_example = ("apple", "banana", "cherry")
print("Type of tuple_example:", type(tuple_example))
print("Length of tuple_example:", len(tuple_example))
print("First element of tuple_example:", tuple_example[0])
print("Last element of tuple_example:", tuple_example[-1])
print("Elements from index 1 to 2 of tuple_example:", tuple_example[1:3])

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

result = convert_seconds(5000)
print(type(result))
h, min, sec = result
print(h, min, sec)

animals = ["cat", "dog", "rabbit"]
chars = 0
for animal in animals:
    chars += len(animal)
print("Total Characters: {}, Average length: {}".format(chars, chars / len(animals)))

winners = ["Alice", "Bob", "Charlie"]
for index, winner in enumerate(winners):
    print("{}. {}".format(index + 1, winner))

def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_emails([("alex@gmail.com", "Alex"), ("shay@example.com", "Shay")]))