class Animals:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eating(self):
        print(f"{self.name} is eating")

    def sleeping(self):
        print(f"{self.name} is sleeping")


class Dog(Animals):
    def speak(self):
        print("woof!!")


class Cat(Animals):
    def speak(self):
        print("meow!!")


class Mouse(Animals):
    def speak(self):
        print("squeek!!")


dog = Dog("Rick")
cat = Cat("Morty")
mouse = Mouse("Jerry")

print(dog.name)
print(cat.is_alive)
mouse.eating()
mouse.sleeping()
cat.speak()
