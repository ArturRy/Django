import csv

def csv_reader():
    result = []
    with open('phones.csv', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for c in reader:
            result.append(c)
    return result


CONTENT = csv_reader()

print(CONTENT)