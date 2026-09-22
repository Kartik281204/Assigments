import math


class Shape():
    def __init__(self, colour, is_filled):
        self.colour = colour
        self.is_filled = is_filled

    def discription(self):
        print(
            f"The colour is {self.colour}  and is it filled ?{self.is_filled}")


class Circle(Shape):
    def __init__(self, colour, is_filled, radius):
        super().__init__(colour, is_filled)
        self.radius = radius

    def discription(self):
        super().discription()
        print(
            f"The circumference of the circle is  {2*math.pi*self.radius:.2f} cms")


class Rectangle(Shape):
    def __init__(self, colour, is_filled, length, width):
        super().__init__(colour, is_filled)
        self.length = length
        self.width = width

    def discription(self):
        super().discription()
        print(
            f"The parameter of the rectangle is {2*self.length*self.width} cms")


class Square(Shape):
    def __init__(self, colour, is_filled, length):
        super().__init__(colour, is_filled)
        self.length = length

    def discription(self):
        super().discription()
        print(f"The parameter of the square is {4*self.length} cms")


class Triangle(Shape):
    def __init__(self, colour, is_filled, length, height):
        super().__init__(colour, is_filled)
        self.length = length
        self.height = height

    def discription(self):
        super().discription()
        print(
            f"The parameter of the triangle is {self.length*self.height} cms")


triangle = Triangle("Blue", True, 6, 8)
circle = Circle("Blue", True, 6)
square = Square("Yellow", False, 9)
rectangle = Rectangle("Black", True, 4, 8)
triangle.discription()
rectangle.discription()
square.discription()
circle.discription()
