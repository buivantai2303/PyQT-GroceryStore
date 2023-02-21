string = input("Enter a string: ").lower()
counts = {}

for letter in string:
    if letter.isalpha():
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1

# print the counts
for letter, count in sorted(counts.items()):
    print(letter + ":" + str(count))
