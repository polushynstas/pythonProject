import json
import csv
import random

with open('dictionary.json', 'r') as json_file:
    json_dictionary = json.load(json_file)

for key, value in json_dictionary.items():
    value += (''.join([str(random.randint(0, 9)) for _ in range(10)]),)


with open('csv_dictionary.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_dictionary = csv.writer(csv_file)
    csv_dictionary.writerow(['ID', "Ім'я", 'Вік', 'Телефон'])

    for key, value in json_dictionary.items():
        csv_dictionary.writerow([key, value[0], value[1], value[2]])
