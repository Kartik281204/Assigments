class Animal():
    def __init__(self, name):
        self.name = name

    def eating(self):
        print(f"This nigga {self.name} eating like he never seen food 😭😭😭 ")

    def sleeping(self):
        print(
            f"This nigga {self.name} sleeping , dawg wake up your ass is gonna be dinner 😭😭😭 ")


class Prey(Animal):
    def fleeing(self):
        print(f"This {self.name} nigga running for his life ")


class Predator(Animal):
    def hunting(self):
        print(f"This {self.name} nigga hunting others what the fuck 😭 ")


class Rabbit(Prey):
    pass


class Hawk(Prey):
    pass


class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Hawk")
hawk = Hawk("LMFAPPP")
fish = Fish("chichu")
fish.fleeing()
