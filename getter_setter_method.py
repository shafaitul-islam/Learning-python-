class Employee:
    company_name = "Ostad Company"
    def __init__(self,name,salary):
        self.name = name
        self._slary = salary
    def get_salary(self,password):
        if password == "admin":
            print(self._slary)
        else:
            print("Invalid Access")

ob1 = Employee("Rahim", 30000)    
ob2 = Employee("Karim", 50000)   

ob1.get_salary("admin")
ob1.slary = 60000
print(ob1._slary)