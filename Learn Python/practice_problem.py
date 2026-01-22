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
#Take two numbers input and print all operations
x = int(input("Enter first number:"))
y = int(input ("Enter second number:"))
print("Addition:",x+y)
print("Subtraction:", x-y)
print("Multiplication:",x*y)
if y==0:
    print("Division: undefined(Division by zero)")
    else:
        print("Division:",x/y)
        print("Floor Division:",x//y)
        print("Modulus:",x%y)
        print("Exponentionation:",x**y)
        #Check memory id of mutable object before and after change
        #solve:
        my_list = [1,2,3]
        print("Before change:", my_list, "ID:", id(my_list))
        my_list.append(4)
        print("After change:", my_list, "Id:", id(my_list))
        #check memory id of immutable object before and after change
        #solve:
        my_string = "Hello world"
        print("Before change:", my_string , "Id:", id(my_string))
        my_string += "!"
        print("After change:", my_string , "Id:", id(my_string))
        # Convert input string to float
        #solve:
        input_str = input("Enter a number:")
        try:
            converted_float = float(input_str)
            print("Converted float:", converted_float)
        except ValueError:
            print("Invalid input. please enter a valid number.")
            #Print formatted output
            #solve:
            product_name = "MacBook Air"
            price = 999.99
            quantity = 2
            print(f"Product:{product_name}, price: ${price}, Quantity:{quantity}",sep='',end='\n')
            # Store different data types in variables and print types.
            product_name = "MacBook Air"
            price = 999.99
            quantity = 2
            is_available = True
            print(type(product_name))
            print(type(price))
            print(type(quantity))
            print(type(is_available))
            # Store large number and check type.
            large_number = 12345676890
            print("Large Number:", large_number, "Type:", type(large_number))
            #Write program to calculate average of 3 numbers
            num1 = float(input ("Enter first number:"))
            num2 = float (input("Enter second number:"))
            num3 = float(input("Enter third number:"))
            avg =(num1+num2+num3)/3
            print("Avarage of three numbers:", avg)