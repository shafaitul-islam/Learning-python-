class Employee:
    company_name = "Default Company"   # class variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"EMP Name: {self.name}\nSalary : {self.salary}")

    @classmethod
    def change_company_name(cls, name):
        cls.company_name = name


ob1 = Employee("Rahim", 30000)
ob1.display_info()

Employee.change_company_name("ABC Company")
print(ob1.company_name)
