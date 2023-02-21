def capitalize_strings(strings):
    return [Text.capitalize() for Text in strings]


strings = input("Enter a list of strings separated by spaces: ").split()
print("Capitalized strings:", capitalize_strings(strings))
