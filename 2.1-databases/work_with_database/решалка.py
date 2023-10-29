import csv

def csv_reader():

    with open('phones.csv', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for c in reader:
            print(c)


# def csv_reader():
#     result = []
#     with open('phones.csv', newline='', encoding='utf-8') as file:
#         fieldname = ['id', 'name', 'image', 'price', 'release_date', 'lte_exists']
#         reader = (csv.reader(file))
#         for row in reader:
#             print(row[0].split(';'))

csv_reader()