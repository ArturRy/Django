import csv

with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)

    CONTENT = [(row['Name'], row['Street'], row['District']) for row in reader]
print(str(CONTENT))