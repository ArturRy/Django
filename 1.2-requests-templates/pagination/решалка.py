import csv

with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    CONTENT = []
    for row in reader:
        CONTENT.append([row['Name'], row['Street'], row['District']])
        # print(row['Street'], row['Name'])
    print((CONTENT))