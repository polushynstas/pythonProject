import math

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __sub__(self, other):
        first_circle = self.x - other.x
        second_circle = self.y - other.y
        return Point(first_circle, second_circle)

    def __str__(self):
        return f'Point ({self.x}, {self.y})'

class Circle(Point):

    def __init__(self, radius, x=0,y=0):
        super().__init__(x,y)
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __str__(self):
        return f'Circle ({self.x}, {self.y} , radius = ({self.radius})'

    def __sub__(self, other):
        if abs(self.radius) == abs(other.radius):
            return super().__sub__(other)
        else:
            rad = abs(self.radius - other.radius)
            new_sub = super().__sub__(other)
            return Circle(rad, new_sub.x, new_sub.y)



