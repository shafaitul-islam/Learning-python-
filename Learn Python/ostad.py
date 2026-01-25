# ---------------- STRING METHODS ----------------
a = "raHim"
b = a.title()

print(a.title())
print(b)
print(a.upper())
print(a.lower())
print(a.swapcase())

txt = "I Like Banana"
x = txt.replace("Banana", "Mango")
print(x)
print(txt)

# ---------------- STRING FORMATTING ----------------
a = "Good Morning, Rahim. How are you?"
user_input = input("What is your name? ")
print(a.replace("Rahim", user_input))
print(a)

age = 23
f_name = "Rahin"
l_name = "Ahmed"
txt = f"I am {f_name} {l_name}. I am {age} years old"
print(txt)

# ---------------- OPERATORS ----------------
a = 4 + 5
b = 6 - 3
c = 4 * 2
d = 8 / 2
e = 5 // 2

print(a, b, c, d, e)

x = (2 + 4) - 5 + 18 / 2 + 12 * 2 - 5 ** 2
print(x)

# ---------------- MATH FUNCTIONS ----------------
import math

print(math.ceil(5.5))
print(math.floor(5.9))
print(round(5.5))

# ---------------- CONDITIONAL STATEMENTS ----------------
rain = 1
if rain == 1:
    print("Take an Umbrella")
else:
    print("No need to take an umbrella")

num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# ---------------- LIST ----------------
a = [1, 2, 3, 'Naim', 'Fahim', 5.8, 6.4]
a[0] = 100
print(a[-1])
print(len(a))

a.append("Rahim")
a.insert(2, "Ostad")
a.remove(5.8)
a.reverse()
print(a)

# ---------------- TUPLE ----------------
t = (1, 2, 3, 4)
print(t)
print(t[2])
# t.reverse() ❌ tuples have no reverse

# ---------------- RANGE ----------------
a = range(10)
b = list(range(10))
c = list(range(1, 10, 2))
d = list(range(10, 0, -1))
e = list(range(100, 2, -2))

print(e)
print(d)
print(list(a))
print(b)
print(c)

# ---------------- FOR LOOP ----------------
for item in range(1, 6):
    print(item)

for char in "hello":
    print(char)

# ---------------- BREAK & CONTINUE ----------------
a = [1, 2, 3, 4, 5, 'a', 6, 7]
for i in a:
    if isinstance(i, str):
        break
    print(i)

for i in a:
    if isinstance(i, str):
        continue
    print(i)

# ---------------- LIST COMPREHENSION ----------------
a = [1, 10, 23, 24, 26, 90]
even_numbers = [i for i in a if i % 2 == 0]
print(even_numbers)

b = [1, 2, 3, 4, 5]
b_new = [i**2 if i % 2 == 0 else i for i in b]
print(b_new)

# ---------------- WHILE LOOP ----------------
a = [1, 2, 3, 4, 5]
total = 0
i = 0

while i < len(a):
    total += a[i]
    i += 1

print(total)

# ---------------- SET ----------------
s = {1, 2, 3, 4, 5, 5}
print(s)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.union(b))
print(a.intersection(b))

# ---------------- DICTIONARY ----------------
person = {'name': 'Rahin', 'age': 23, 'city': 'Dhaka'}
person['age'] = 24
person['profession'] = 'Student'

for key, value in person.items():
    print(f"{key}: {value}")

# ---------------- ZIP ----------------
keys = [1, 2, 3]
values = ['mango', 'banana', 'orange']
print(dict(zip(keys, values)))

# ---------------- DICTIONARY COMPREHENSION ----------------
nums = list(range(11))
result = {i: "Even" if i % 2 == 0 else "Odd" for i in nums}
print(result)

# ---------------- FUNCTIONS ----------------
def my_first_function():
    print(10 + 20)

my_first_function()

def add_two_numbers(a, b):
    return a + b

print(add_two_numbers(22, 12))

def mul_two_numbers(a, b):
    return a * b

print(mul_two_numbers(5, 6))

def hello():
    return "Hello World"

print(hello())

def addition(*args):
    return sum(args)

print(addition(1, 2, 3, 4, 5))

def my_func(**kwargs):
    print(f"My name is {kwargs['f_name']} {kwargs['l_name']}")

my_func(f_name="Shafaitul", l_name="Islam")

# ---------------- LAMBDA ----------------
square = lambda x: x ** 2
print(square(5))

# ---------------- MAP & FILTER ----------------
nums = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * x, nums)))

nums = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x: x % 2 == 0, nums)))

# ---------------- FILE HANDLING ----------------
with open("sample.txt", "r") as file:
    print(file.read())
#------------------  Writing in a File ------------
with open ('name.txt','w') as f:
    f.write("Hello world\n")
    f.write("I am writing in a file \n")