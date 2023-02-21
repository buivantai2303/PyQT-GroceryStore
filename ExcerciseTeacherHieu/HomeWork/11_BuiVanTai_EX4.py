def count_strings(strings):
    count = 0
    for s in strings:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    return count


string_list = input("Enter a list of strings separated by commas: ").split(',')
string_list = [s.strip() for s in string_list]
num_strings = count_strings(string_list)
print("Number of strings meeting the criteria:", num_strings)
