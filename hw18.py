import json
dictionary = {
    123456: ('Sam', 25),
    234567: ('Tom', 30),
    345678: ('Smith', 22),
    456789: ('Jack', 28),
    567890: ('Emily', 35)
}

with open('dictionary.json', 'w') as f:
    json.dump(dictionary, f)