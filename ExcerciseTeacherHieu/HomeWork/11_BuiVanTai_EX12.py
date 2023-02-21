def Remove(string):
    vowels = "ueoaiUEOAI"
    result = ""
    for char in string:
        if char not in vowels:
            result += char
    print("String with vowels removed:", result)


string = input("Enter a string: ")
Remove(string)