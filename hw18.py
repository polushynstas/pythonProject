import json

dictionary = {
    123456: ('Іван', 25),
    234567: ('Марія', 30),
    345678: ('Петро', 22),
    456789: ('Ольга', 28),
    567890: ('Андрій', 35)
}

with open('dictionary.json', 'w') as f:
    json.dump(dictionary, f)