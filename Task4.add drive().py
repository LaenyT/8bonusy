class Car:
    def __init__(self, make, model, year, color, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage

    def display_car(self):
        print(f"make: {self.make}")
        print(f"model: {self.model}")
        print(f"year: {self.year}")
        print(f"color: {self.color}")
        print(f"mileage: {self.mileage} miles")

        print("\n")

    def drive(self,distance):
        self.mileage += distance
        print(f"New mileage: {self.mileage} miles")

car1 = Car("Toyota", "Camry", 2023, "Black", 1500)
car2 = Car("Daewoo", "Nexia", 1945, "white", 4500)
print("\n")
print("Information about Car 1:")
car1.display_car()

car1.drive(100)


print("Information about Car 2:")
car2.display_car()

car2.drive(200)