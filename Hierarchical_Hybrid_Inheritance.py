class Vehicle:
    def engine_type(self):
        print("Vehicle is a engine")
class Car(Vehicle):
    def num_doors(self):
        print("Car has 4 doors")

class Truck(Vehicle):
    def load_capacity(self):
        print("Truck Can carry 10 tons")
car = Car()
car.engine_type()
car.num_doors()
truck = Truck()
truck.engine_type()
truck.load_capacity()

#Hybrid

class Shape:
    def area(self):
        print("Claculating area...")

class Polygon(Shape):
    def side(self):
        print("Polygon has multiple sides.")

class Rectangle(Polygon):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
        super().__init__()
    def area(self):
        return self.length*self.breadth
    
rec = Rectangle(10,5)
rec.side()
print(rec.area())