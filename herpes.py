class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def width(self):
        return f"{self._width:.2f}"

    @property
    def length(self):
        return f"{self._length:.2f}"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = self.new_width
        else:
            print("The width must be greater than 0")

    @length.setter
    def length(self, new_length):
        if new_length > 0:
            self._length = self.new_length
        else:
            print("The length must be greater than 0")

    @width.deleter
    def width(self):
        del self._width
        print("Width of the rectangle has been deleted ")

    @length.deleter
    def length(self):
        del self._length
        print("Length of the rectangle has been deleted ")


rectangle = Rectangle(3, 4)
rectangle.width = 0
rectangle.length = -1
print(rectangle.length)
print(rectangle.width)
del rectangle.length
del rectangle.width
