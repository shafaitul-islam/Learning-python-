class Car:
    def __init__(self, brand, model, year, number_of_doors):
        self.brand = brand
        self.model = model
        self.year = year
        self.number_of_doors = number_of_doors

    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")


class Motorcycle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Motorcycle is starting")

    def stop(self):
        print("Motorcycle is stopping")
vehicles = [
    Car("Ford", "Focus", 2008, 5),
    Motorcycle("Honda", "Scoopy", 2018)
]

for vehicle in vehicles:
    print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
    vehicle.start()
    vehicle.stop()
