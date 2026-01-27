class Car:
    def __init__(self, model="Honda", brand="Civic"):
        self.model = model
        self.brand = brand

    def display_info(self):
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")

car1 = Car("Toyota", "Corolla")
car1.display_info()
