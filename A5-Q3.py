#Question 3
#Area of a triangle

import math
a=int(input("Enter first side of the triangle: "))
b=int(input("Enter second side of the triangle: "))
c=int(input("Enter third side of the triangle: "))
if a<0 or b<0 or c<0:
    print("Invalid input, side cannot be negative")
elif a+b<c or b+c<a or c+b<a: #Checking whether the sides satisfy the triangle inequality
    print("Combination of sides is not possible")
else:
    s=(a+b+c)/2 #Calculating semi perimeter
    area=math.sqrt(s*(s-a)*(s-b)*(s-c)) #Heron's formula
    print(f"Area of the triangle is {area}")
    print()
