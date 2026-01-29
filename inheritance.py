# Single Inheritance

class GrandFather:
    def __init__(self, color, first_name):
        self.color = color
        self.first_name = first_name
    def gf_method(self):
        print("I am From Grandfather")

class Father(GrandFather):
    def __init__(self, hobby, color, first_name):
        super().__init__(color, first_name)   # ✅ pass arguments
        self.hobby = hobby
    def father_method(self):
        print("I am From Father")
class Children(Father,GrandFather):
    def __init__(self, fashion,hobby,color,first_name):
       super().__init__(hobby,color,first_name)
       self.fashion = fashion


gf1 = GrandFather("Red", "Chowdhury")
f1 = Father("Cricket", "Red", "Chowdhury")
c1 = Children("Test","Badminton","Red","Chowdhury")
print(f1.color)
c1.gf_method()
c1.father_method()
print(c1.fashion , c1.color,c1.hobby,c1.first_name)

