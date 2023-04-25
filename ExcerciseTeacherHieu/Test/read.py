def readfile(filename):
    with open(filename, 'r', encoding='utf-8',) as file:
        return file.readline()


print(readfile('input01.txt'))

