def FindMax(NumList):
    Max = NumList[0]
    for number in NumList:
        if number > Max:
            Max = number
    return Max

NumList = [int(number) for number in input("Enter a list of numbers separated by spaces: ").split()]
print("Largest number:", FindMax(NumList))