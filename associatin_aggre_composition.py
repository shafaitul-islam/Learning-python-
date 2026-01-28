# Association

class Laptop:
    def __init__(self, brand):
        self.brand = brand
        
class Student:
    def __init__(self, name, laptop_obj):
        self.name = name
        self.laptop_v = laptop_obj

    def show_laptop(self):
        print(f"{self.name} has a laptop named {self.laptop_v.brand}")


lp1 = Laptop("Asus")                 
student = Student("Rahim", lp1)     
student.show_laptop()

#Aggregation : Has a relationship

class Department:
    def __init__(self, name):
        self.name = name


class University:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def show_departments(self):
        return [dept.name for dept in self.departments]


# Create University
un1 = University("ABC University")

# Create Departments
d1 = Department("CSE")
d2 = Department("EEE")
d3 = Department("BBA")

# Add departments to university
un1.add_department(d1)
un1.add_department(d2)
un1.add_department(d3)

# Show departments
print("Departments in", un1.name, "are:")
print(un1.show_departments())

#composition
class Engine:
    def __init__(self, power):
        self.power = power

    def show_engine(self):
        print("Engine power:", self.power)


class Car:
    def __init__(self, brand):
        self.brand = brand
        self.engine = Engine("1500cc")   # ✅ Engine created inside Car (Composition)

    def show_car(self):
        print("Car brand:", self.brand)
        self.engine.show_engine()


# Create Car object
car1 = Car("Toyota")
car1.show_car()
