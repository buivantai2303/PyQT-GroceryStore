def count_word(lst, letter):
    count = 0
    for word in lst:
        if word.startswith(letter):
            count += 1
    return count


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


input01 = read_file('input01.txt').split()
input02 = read_file('input02.txt').split()

count_a_input01 = count_word(input01, 'a')
count_a_input02 = count_word(input02, 'a')

print("Number of words that start with the letter a in file input01.txt:", count_a_input01)
print("Number of words that start with the letter a in file input02.txt:", count_a_input02)
if count_a_input01 > count_a_input02:
    print('And result is input01.txt has more words that start with the letter "a".')
elif count_a_input01 < count_a_input02:
    print('And result is input02.txt has more words that start with the letter "a".')
else:
    print('And result is both files have the same number of words that start with the letter "a".')
