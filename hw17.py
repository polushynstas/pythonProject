line_1 = input('Введіть перший рядок: ')
line_2 = input('Введіть другий рядок: ')
line_3 = input('Введіть третій рядок: ')
line_4 = input('Введіть четвертий рядок: ')

with open('hw17.txt', 'w') as file:
    file.write(line_1 + '\n')
    file.write(line_2 + '\n')

with open('hw17.txt', 'a') as file:
    file.write(line_3 + '\n')
    file.write(line_4 + '\n')

