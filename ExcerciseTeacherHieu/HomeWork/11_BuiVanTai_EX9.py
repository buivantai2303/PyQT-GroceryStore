string = input("Enter a string: ")
result = ""

for letter in string:
    if letter.islower():
        result += letter.upper()
    elif letter.isupper():
        result += letter.lower()
    else:
        result += letter

print("Result:", result)
