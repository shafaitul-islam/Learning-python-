class Employee:
    company_name = "Ostad Company"

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary   

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        self.__salary = new_salary


ob1 = Employee("Rahim", 40000)

print(ob1.salary)       

ob1.salary = 70000       

print(ob1.salary)        
