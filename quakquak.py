class Animals():
    alive = True


class Cat(Animals):
    def speak(self):
        print("Meow🐱")


class Dog(Animals):
    def speak(self):
        print("Woof🐶")


class Cow(Animals):
    def speak(self):
        print("Mooooooo🐄")


class Mouse(Animals):
    def speak(self):
        print("Squeeeek Squeek")


class Bat(Animals):
    def speak(self):
        print("ZZZZZZZZZZZZZZ🦇")


class Hyena(Animals):
    def speak(self):
        print("HHEHEHHEHEHEHEHEH😆")


class Lion(Animals):
    def speak(self):
        print("Roooooooooooooaaaarrrrrrrrrrrr🦁")


class Car():
    def speak(self):
        print("HOOOOONKKKKKK🚗")
    alive = False


animals = [Lion(), Bat(), Hyena(), Cat(), Dog(), Cow(), Mouse(), Car()]
for animal in animals:
    animal.speak()
    print(animal.alive)
