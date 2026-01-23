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

# string formating
a="Good Morning,Rahin. How are you?"
user_input = input("what is your Naame?")
print(a.replace("Rahim", user_input))
print(a)

age =23
f_name = "Rahin"
l_name = "Ahmed"
txt = f"I am {f_name} {l_name}. I am {age} years old"

#operators
a= 4+5
b= 6-3
c= 4*2
d= 8/2
e=5//2 #integer division
print(a,b,c,d,e)

x = (2+4) - 5+ 18/2 + 12*2 -5**2
print(x)
#Math functions
import math

#ceil
x =5.5
print(math.ceil(x))

#floor
y=5.9
print(math.floor(y))

#round

z=5.5
print(round(z))

#conditional statements

rain = 1
if rain == 1:
    print("Take an Umbrella")
    else:
        print("No need to take an umbrella")
# check number is  positive or negative & zero
 num = int(input("Enter a number:"))
 if num > 0:
    print("positive number")
    else if num < 0:
    print("Negative Number")
    else:
        print("Zero")

# List and Tuples
# List
a = [1,2,3,'Naim', 'Fahim',5.8,6.4]
a[0] = 100
print(a[-1])
print(len(a))
a.append("Rahim")
a.insert(2,"Ostad")
a.remove(5.8)
a.reverse()
print(a)
#tuple
t = (1,2,3,4)
print(t)
print(t[2])
tr=t.reverse()
print(tr)

#Range method

a = range(10)
b= list(range(10))
c= list(range(1,10,2))
d= list(range(10,0,-1))
e= list(range(100,2,-2))
print(e)
print(d)
print(a)
print(b)
print(c)

#for loop

a= [1,2,3,4,5,6,7,8,9,10]
for item in a:
    print(item)
b = "hello"
for char in b:
    print(char)
    for i in range(1,1001):
        print(i)

        for i in range(101):
            print(f"Nasa is Haking...{i}% completed")
            print("Nasa is Haked..")
            #Break and continue

            a = [1,2,3,4,5,'a',6,7,8,9]
            for i in a:
                if type(i) == type('b'):
                    break
                else:
                    print(i)
                    for i in a:
                        if type(i) == type('b'):
                            continue
                        else:
                            print(i)
                            #list comprehension
                            a = [1,10,23,24,26,90]
                            result = []
                            for i in a:
                                if i % 2 == 0:
                                    result.append(i)
                            print(result)
                       # list comprehension way
                       a = [1,10,23,24,26,90]
                       new_result = [i for i in a if i % 2 == 0]
                       print(new_result)
                        b=[1,2,3,4,5]
                        b_new = [i**2 if i%2==0 else i for i in b]
                        print(b_new)

                        #while loop
                        a=[1,2,3,4,5,6,7,8,9]
                        result = 0
                        i=0
                        n = len(a)
                        while i < n:
                            result += a[i]
                            i +=1
                            print(result)
                            a= [-10, 2,19,4,-5,6,-7,8,9]
                            i=0
                            while i < len(a):
                                if a[i] < 0:
                                    print(f"Negative number found:{a[i]}")
                                    break
                                i +=1
                            else:
                                print("No negative number found")
                                #set
                                s = {1,2,3,4,5,5,4,3,2,1}
                                print(s)
                                #union AND intersection
                                a = {1,2,3,4}
                                b = {3,4,5,6}
                                print(a.union(b))
                                print(a.intersection(b))
                                #dictionary
                                a = {'name':'Rahin', 'age':23, 'city':'Dhaka'}
                                print(a['name'])
                                a['age'] = 24
                                print(a)
                                a['profession'] = 'Student'
                                print(a)
                                for key in a:
                                    print(f"{key}:{a[key]}")
                                    for key, value in a.items():
                                        print(f"{key}:{value}")
                                    print(-----------------------)
                                    a=[1,2,3]
                                    b=['mango','banana','orange']
                                    print(dict(zip(a,b)))
                                    #dictionary comprehension
                                    num =list(range(0,11))
                                    result = {i: "Even" if i%2==0 else "odd" for i in mun}
                                    print(result)
                                    