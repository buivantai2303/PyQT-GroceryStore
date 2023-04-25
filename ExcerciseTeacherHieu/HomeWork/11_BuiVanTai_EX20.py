import re


with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w', encoding='utf-8') as output_file:
    date_pattern = r'\b\d{2}/\d{2}/\d{4}\b'

    for line in input_file:
        dates = re.findall(date_pattern, line)

        for date in dates:
            output_file.write(f"{date}\n")

print("Dates extracted and written to output.txt.")
