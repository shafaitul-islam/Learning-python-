
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

    
