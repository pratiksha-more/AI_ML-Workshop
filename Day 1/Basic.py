
#Single Line Comment


print("Hello")
city_Name="New Delhi"
x=20.9
z=36

print(x)
print(z)
print(city_Name)


x,y,z=1,2,3

print(x)
print(y)
print(z)


#Cheak Type Of Particular Data Type  :
a=5
print("Type of a: ",type(a))

b=5.0
print("Type of b: ",type(b))

c=2+4j
print("Type of a: ",type(c))

#Boolean Data Type 

print(type(True))
print(type(False))
print(type(None))
# print(type(true)) Invalide

#Arithmetic Operator

print(9%2)
print(9//4)
print(9/4)

#User Input

name=input("Enter Your Name: ")
print("Hello",name)


#Syntax of Input 
num=input("Enter Number: ")
print("Number is: ",num)
print("Type of Number is: ",type(num))

#Type Casting
num=int(input("Enter Number: "))
print("Number is: ",num)
print("Type of Number is: ",type(num))

# -------------------------RANGE--------------------

for i in range(9):
    print(i)

    #using range(start,stop,step  )
print("***Even Number*** ")
for i in range(1,10,2):
    print(i)

print("***Table of 9 *** ")
for i in range(9,91,9):
    print(i)

print("***Table Of 3*** ")
for i in range(3,31,3):
    print(i)


# -------------------------WHILE--------------------

print("***Whike Loop*** ")
count=0
while count<5:
    print(count)
    count+=1

    #************Lab Activity 03 ************
    #function

    def find_square(num):
        return num*num
        return result
    
    square=find_square(5)
    print("Square is: ",square)


