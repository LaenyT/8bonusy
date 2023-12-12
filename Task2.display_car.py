class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_car(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print("\n")

car1 = Car("Toyota", "Camry", 2022)

print("Info about Car 1:")
car1.display_car()

