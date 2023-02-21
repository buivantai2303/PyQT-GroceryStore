def Lambda(strings):
    Result = list(filter(lambda x: len(x) >= 5, strings))
    print(Result)


string = input("Enter a list of strings separated by spaces: ").split(" ")
Lambda(string)

