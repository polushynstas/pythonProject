import time

class Auto:
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

class Truck(Auto):
    def __init__(self, brand, age, mark, color, weight, max_load=4000):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def attention(self):
        print('Attention')
        super().move()

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)

class Car(Auto):
    def __init__(self, brand, age, mark, color, weight, max_speed=1):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def max_speed(self):
        super().move()
        print(f'Max speed is {self.max_speed}')

truck_1 = Truck('Ford', 4, 'Range', 'white', 3500, 5000)
truck_2 = Truck('Tesla', 5, 'Cybertruck ', 'silver', 3400, 2832 )
car_1 = Car('Nissan', 6, 'Rogue', 'black', 1553, 200)
car_2 = Car('Fiat', 7, '500', 'yellow', 1200, 180)

print(f'first Truck brand: {truck_1.brand}')
print(f'first Truck age: {truck_1.age}')
print(f'first Truck color: {truck_1.color}')
print(f'first Truck mark: {truck_1.mark}')
print(f'first Truck weight: {truck_1.weight}')
print(f'first Truck max load: {truck_1.max_load}')
truck_1.move()
truck_1.stop()
truck_1.birthday()
print(f'Age of first Truck after birthday: {truck_1.age}')
truck_1.load()

print(f'second Truck brand: {truck_2.brand}')
print(f'second Truck age: {truck_2.age}')
print(f'second Truck color: {truck_2.color}')
print(f'second Truck mark: {truck_2.mark}')
print(f'second Truck weight: {truck_2.weight}')
print(f'second Truck max load: {truck_2.max_load}')
truck_2.move()
truck_2.stop()
truck_2.birthday()
print(f'Age of ssecond Truck after birthday: {truck_2.age}')
truck_2.load()

print(f'first Car brand: {car_1.brand}')
print(f'first Car age: {car_1.age}')
print(f'first Car color: {car_1.color}')
print(f'first Car mark: {car_1.mark}')
print(f'first Car weight: {car_1.weight}')
print(f'first Car max speed: {car_1.max_speed}')
car_1.move()
car_1.birthday()
print(f'Age of first Car after birthday: {car_1.age}')
car_1.stop()

print(f'second Car brand: {car_2.brand}')
print(f'second Car age: {car_2.age}')
print(f'second Car color: {car_2.color}')
print(f'second Car mark: {car_2.mark}')
print(f'second Car weight: {car_2.weight}')
print(f'second Car max speed: {car_2.max_speed}')
car_2.move()
car_2.birthday()
print(f'Age of second Car after birthday: {car_2.age}')
car_2.stop()

    