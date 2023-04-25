import csv
import re

email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

with open('data.csv', 'r', newline='', encoding='utf-8') as csv_file, open('output.txt', 'w',
                                                                           encoding='utf-8') as output_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        email = row['email']

        if re.match(email_pattern, email):
            output_file.write(f"{email}\n")

print("Valid email addresses extracted and written to output.txt.")
