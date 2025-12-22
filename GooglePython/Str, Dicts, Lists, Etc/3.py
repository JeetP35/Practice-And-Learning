str3 = "Hello World! I'm learning Python."
str3.upper()
print("Uppercase string:", str3.upper())

str3.lower()
print("Lowercase string:", str3.lower())

str3.strip()
print("String after strip (no effect here):", str3.strip())

str3.lstrip()
print("String after lstrip (no effect here):", str3.lstrip())

str3.rstrip()
print("String after rstrip (no effect here):", str3.rstrip())

str3.count("e")
print("Count of 'e' in string:", str3.count("e"))

str3.startswith("Hello")
print("Does the string start with 'Hello'?:", str3.startswith("Hello"))

str3.endswith("Python.")
print("Does the string end with 'Python.'?:", str3.endswith("Python."))

str3.isnumeric()
print("Is the string numeric?:", str3.isnumeric())

print("Joined string with space:", "".join(["Hello", "World"]))
print("Joined string with space:", " ".join(["Hello", "World"]))

str3.split(" ")
print("String split by space:", str3.split(" "))