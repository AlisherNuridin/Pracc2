import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

n = int(input())
x = Circle(n)

print(f"{x.area():.2f}")
