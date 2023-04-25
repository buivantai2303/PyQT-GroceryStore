import collections

with open('Context.txt', 'r', encoding='utf-8') as file:
    try:
        word_counts = collections.Counter()

        for line in file:
            words = line.split()

            word_counts.update(words)

        for i, (word, count) in enumerate(word_counts.items(), 1):
            print(f"{i}. '{word}' occurs {count} times.")
    except UnicodeDecodeError as e:
        print(f'Error on line {e.start}: {e.object[e.start:e.end]}')
