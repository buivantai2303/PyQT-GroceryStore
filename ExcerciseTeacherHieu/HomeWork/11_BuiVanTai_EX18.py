import codecs

def print_lines_with_word(file_path, word):
    with codecs.open(file_path, encoding='utf-8') as file:
        for line in file:
            if word in line:
                print(line.strip())


file_path = 'Context.txt'  # replace with your file path
word = 'lá'  # replace with your desired word
print_lines_with_word(file_path, word)

