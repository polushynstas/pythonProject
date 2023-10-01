import openpyxl
import csv

with open('csv_dictionary.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    work_book = openpyxl.Workbook()
    sheet = work_book.active

    for row in csv_reader:
        row.pop(2)
        sheet.append(row)

    work_book.save('xlsx_dictionary.xlsx')
