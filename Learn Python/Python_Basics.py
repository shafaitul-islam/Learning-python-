
#  First Program in Python
print("Hello, World!")
#Variables and Datas Types
name= "Shafaitul"
age = 23
cgpa =3.00
is_student = True
print("Name:", name)
print("Age:",age)
print("CGPA:",cgpa)
print("Is Student:",is_student)
print(type(name),type(age),type(cgpa),type(is_student))
#Type Convertions
x ="10"
y = int(x)
print("Converted Value:",y+5)
#Math Operations
a=20
b= 15
print("Addition:",a+b)
print("Subtraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
print("Floor Division:",a//b)
print ("Modulus:",a%b)
print("Exponentiation:",a**b)
#Input from User
user_name = input ("Enter Your name:")
user_age = input ("Enter Your age:")
print("user Name:",user_name)
print("user Age:",user_age)
#convart string to integer
f = "25"
s = int(f)
print("Sum:", s+10)
print("Type Of S:", type(s))
#check type of user input
x= input("Enter a Value:")
y = input ("Enter Another Value:")
print("Type of X:", type(x))
print("Type of Y:", type(y))
#Change value of a list
my_list =["shafayet",23,5.7,"CSE Student",True ]
print("Orginal List:",my_list)
my_list[2]= 5.9
print("Updated List:",my_list)  

#string ,conditions & loops

# string Methods

text = "python Programming is fun"
print("Orginal Text:",text)
print("UpperCase:", text.upper())
print("LowerCase:", text.lower())
print("TitleCase:", text.title())
print("Count of 'o':", text.count('o'))
print("Find 'Programming':", text.find('Programming'))
print("Replace 'fun' with 'awesome':", text.replace('fun','awesome'))

name = "Shafaitul Islam"
age = 23
print(f"My name is {name} and I am {age} years old.")
# If conditions
num =10
if num%2==0:
    print("Even Number")
    else:
        print("Odd Number")
# while Loop
 i= 1
 while i<=100:
    print(i)
    i+=1
    # for loop
    for j in range(1,6):
        print(j)  

#Loops and Built-in Data Structures
#For loop 
for n in range (1,5):
    print(n)

#list
nums = [10,20,30,40,50]
nums.append(60)
print("List after Append:",nums)
nums.remove(30)
print("List after Remove:",nums)


#list compoarison
squares = [x**2 for x in range(1,6)]
print("Squares List:", squares)


#tuple
colors = ("Red","Green","Blue")
print("Tuple Colors:", colors)

#set
fruts = {"Apple","Bannana", "Orange"}
print("Set of Frutes:", fruts)
fruts.add("Mango")
print("Set after Add:",fruts)
fruts.remove("Bannana")
print("Set after Remove:",fruts)

#dictionary
student = {
    "name": "Shafaitul Islam",
    "age": 23,
    "cgpa": 3.00
}
print("Dictionary Student :", student)

student["cgpa"] = 3.20
print("Updated Dictionary Student:", student)
print("Student Name:", student["name"])

#Loop through Dictionary

for key, value in student.items():
    print(f"{key}:{value}")

# Functions 
def add(a,b):
    return a+b
print("sum:", add(12,34))

def greet (name):
    print(f"Hello, {name}")
    greet("Shafaitul")

#Lambda Function
square = lambda x: x*x
print("Square of 5:", square(5))

#Map Function
numbers = [1,2,3,4,5]
squared_numbers = list(map(lambda x: x**2, numbers))
print("squared Numbers:", squared_numbers)

#Filter Function
even_numbers = list(filter(lambda x: x%2==0, numbers))
print("Even Numbers:", even_numbers)

#list comprehension
cubes = [x**3 for x in range(1,6)]
print("Cubes List:", cubes)

#File Writing and Reading 
#writing to a file
file = open("data.txt","w")
file.write("Hello, this is a sample file.\n")
file.write("This file is created using python.\n")
file.close()
#Reading from a file
file = open("data.txt","r")
print(file.read())
file.close()

#Appending to a file
file = open("data.text","a")
file.write("Appending a new line to the file.\n")
file.close()

#Reading the update file
file = open("data.txt","r")
print(file.read())
file.close()

#Exception Handling
try:
    x = int(input("Enter a Number:"))
    print("10 divided by", x, "is", 10/x)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        except ValueError:
            print("Error: Invalid input. please enter a valid number.")
#Finally Block
finally:
    print("Execution Completed.")

#Modules , json Date and Apis

import math
print("Square Root of 13:", math.sqrt(13))
print("Value of PI:", math.pi)

import json
data = {
    "name": "Shafaitul Islam",
    "age": 23,
    "department": "CSE",
    "cgpa": 3.00
}
with open("student.json","w") as f:
    json.dump(data,f)
    from datetime import datetime
    print("Current Date and Time:", datetime.now())

    import requests 
    response = requests.get("https://api.github.com")
    print("GitHub API Status Code:", response.status_code)
    print("GitHub API Response:", response.json())
#OOp and Design Patterns

#class Example
class student:
    def__init__(self,name,age):
     self.name = name
     self.age = age
     def show__info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        #Creating an object
        s1 = student("Firus Anika Nesho",17)
        s1.show_info()
        #Inheritance Example
        class person:
            def__init__(self,name):
            self.name = name
            def greet(self):
                print(f"Hello, my name is {self.name}")
                class employee(person):
                    def__init__(self,name,position):
                        super().__init__(name)
                        self.position = position
                        def show_position(self):
                            print(f"Position: {self.position}")
                            e1 = employee("Shafaitul Islam", "software Engineer")
                            e1.greet()
                            e1.show_position()

                            #Design Pattern Example: singleton
                            class singletion:
                                __instance = None
                                def__new__(cls, *args, **kwargs):
                                    if not cls.__instance:
                                        cls.__instance = supper(singletion,cls).__new__(cls)
                                        return cls.__instance
                                        obj1 = singleton()
                                        obj2 = singleton()
                                        print("Are both objects same?", obj1 is obj2)
                                        

                    