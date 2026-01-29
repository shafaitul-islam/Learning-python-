#Singleton

class Singletion:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            print("1st object is created")
            cls._instance = super(Singletion,cls).__new__(cls)

ob1 = Singletion()
ob2 = Singletion()

print(ob1 is ob2)

#Factory Design Pattern

class Car:
    def drivier(self):
        return "Draiving a car"

class Bike:
    def driver(self):
        return "Riding a bike"
    
class VehicleFactory:
    @staticmethod
    def get_vechile(type):
        if type == "car":
            return Car()
        elif type == "bike":
            return Bike()
        else:
            return ValueError("Unknown Vehicle")
        
vechicle = VehicleFactory.get_vechile("car")
print(vechicle.driver())

#Builder Design pattern

# Builder Design Pattern

class Computer:
    def __init__(self, cpu, ram, storage):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage

    def show_config(self):
        print(f"CPU: {self.cpu}")
        print(f"RAM: {self.ram}")
        print(f"Storage: {self.storage}")


class ComputerBuilder:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None

    def set_cpu(self, cpu):
        self.cpu = cpu
        return self        # ✅ method chaining

    def set_ram(self, ram):
        self.ram = ram
        return self

    def set_storage(self, storage):
        self.storage = storage
        return self

    def build(self):
        return Computer(self.cpu, self.ram, self.storage)


# ✅ Using the Builder
builder = ComputerBuilder()
computer = builder.set_cpu("Intel i7") \
                  .set_ram("16GB") \
                  .set_storage("1TB SSD") \
                  .build()

computer.show_config()
