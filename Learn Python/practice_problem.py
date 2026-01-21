# print your name, age, and city in separate lines also slow the type of each variable.
#solve:
name="M Shafaitul Islam"
age = 23
city = "Dhaka"
print("Name:",name)
print("Age:",age)
print("City:",city)
print(type(name),type(age), type(city))
# swap two variables
#solve:
a=10
b=20
print("Before Swaping :", "A =",a,"B =",b)
a,b =b,a
print("After Swaping:","A =",a,"B =",b)
# Take Two Numbers Input and Print All Operations
#solve:
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))
print("Addition:",num1+num2)
print("Subtraction:",num1-num2)
print("Multiplication:",num1*num2)
if num2==0:
    print("Division: undefined(Division by zero)")
else:
    print("Division:",num1/num2)
    print("Floor Divisioin:",num1//num2)
    print("Modulus:",num1%num2)
    print("Exponentionation:",num1**num2)
 #Print Formatted Output
 # solve:
first_name = "M Shafaitul"
last_name = "Islam"
age = 23
city = "Dhaka"
print(f"My Name is {first_name} {last_name}. I am {age} years old and I live in {city}.")