string = input("Enter a string: ")

if string[0] == string[-1]:
    print(string[1:-1])
else:
    print(string)