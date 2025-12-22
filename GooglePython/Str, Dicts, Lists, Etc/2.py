str1 = "Hallo World! I'm learning Python."
print("Original string:", str1)

new_str1 = str1[0:1] + "e" + str1[2:]
print("After replacing character at index 2:", new_str1)

str2 = "Hello World! I'm learning Python."
print("Original string:", str2)

print(str2.index("World"))
new_str2 = str2[0:6] + "Universe" + str2[11:]
print("After replacing 'World' with 'Universe':", new_str2)

# Example : Replace domain in email address
'''
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email
'''