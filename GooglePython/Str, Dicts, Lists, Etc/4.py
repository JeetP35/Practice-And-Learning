name = "Dogeshwar"
number = len(name) * 67
print("Hello {}, your number is {}".format(name, number))

print("Your name is {name} and your number is {num}".format(name=name, num=number))

price = 49.99
with_tax = price * 1.07
print("Price: ${:.2f}, Price with tax: ${:.2f}".format(price, with_tax))