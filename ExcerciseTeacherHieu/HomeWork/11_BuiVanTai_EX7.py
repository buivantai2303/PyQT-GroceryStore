if __name__ == '__main__':
    PUT = int(input("Enter integer number: "))
    print("Factors of", PUT,":", end=' ')

    for i in range(0, PUT):
        i += 1
        if PUT % i == 0:
            print(i, end=', ')
