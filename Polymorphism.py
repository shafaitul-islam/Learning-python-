class Grandfather:
    def greet(self):
        print("Grandfather says")

class Father(Grandfather):
    def greet(self):
        print("Father says")

class Children(Father):
    def greet(self):
        print("Children says")

class Person:
    def __init__(self, f_name=None, l_name=None):
        if f_name and l_name:
            self.f_name = f_name
            self.l_name = l_name
        else:
            self.name = "Rahim"

p1 = Person()
print(p1.name)

p2 = Person("Md", "Rahim")
print(p2.f_name, p2.l_name)
