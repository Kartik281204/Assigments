class Car:
    def __init__(self, model, year, colour, for_sale):
        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the car {self.colour} {self.model}")
        print("Hope you are not a woman")

    def stop(self):
        print(f"You stopped the {self.model} ")
        print(f"Damn!! that was too harsh are you a woman?")

    def description(self):
        print(self.model)
        print(self.year)
        print(self.colour)
