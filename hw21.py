class Car:
    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print('move')
    def stop(self):
        print('stop')
    def birthday(self):
        self.age += 1
