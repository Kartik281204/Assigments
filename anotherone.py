import math
from abc import ABC, abstractmethod


class Shapes(ABC):
    @abstractmethod
    def area(self):
        print("The Area is :")


class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)


class Rectangle(Shapes):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Square(Shapes):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


class Triangle(Shapes):
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def area(self):
        return 2 / (self.length*self.height)


class Pizza(Circle):
    def __init__(self, toppings, radius):
        super().__init__(radius)
        self.toppings = toppings


shapes = [Circle(9), Square(10), Rectangle(
    2, 8), Triangle(3, 3), Pizza("peperoni", 9)]
for shape in shapes:
    print(shape.area())
