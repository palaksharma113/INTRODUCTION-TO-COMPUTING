#1 A program to convert a number in it's binary equivalent.
num = int(input("Enter a number\n"))
binary_equivalent = bin(num)
print(binary_equivalent)
print(binary_equivalent[2:])

#2 python calculator
print('1 : addition')
print('2 : subtraction')
print('3 : multiplication')
print('4 : division')

choice = input('enter your choice\n')

num1 = float(input('Enter first number\n'))
num2 = float(input('Enter second number\n'))

if choice == '1':
    print( num1, '+', num2, '=', num1+num2 )
elif choice == '2':
    print(num1, '-', num2, '=', num1-num2 )
elif choice == '3':
    print(num1, '*', num2, '=', num1*num2)
elif choice == '4':
    if num2 ==0:
        print('infinite')
    else:
        print(num1, '/', num2, '=', num1/num2)
else:
    print('invalid choice')

#3
import math

n = 10
r = 10
α = 10
β = 10
y2 = 20
y1 = 10
x2 = 30
x1 = 10

exp1 = (3+4) * (5)
exp2 = ((n)*(n-1)) / 2
exp3 = 4*(math.pi) * (math.pow(r,2))
exp4 = math.sqrt(r*(math.pow(math.cos(α), 2)) + r*(math.pow(math.sin(β), 2)))
exp5 = (y2 - y1)/(x2 - x1)

print(exp1)
print(exp2)
print(exp3)
print(exp4)
print(exp5)

#4

for i in range(5):
    print(i, end=" ")
print()

for i in range(3,10):
    print(i, end=" ")
print()

for i in range(4,13,3):
    print(i, end=" ")
print()

for i in range(15,5,-2):
    print(i, end=" ")
print()

for i in range(5,3):
    print(i, end=" ")

#5
No_H = int(input('Enter number of Hydrogen Atoms: '))
No_C = int(input('Enter number of Carbon Atoms: '))
No_O = int(input('Enter number of Oxygen Atoms: '))

print('Molecular weight of compound is:', (No_H * 1.00794) + (No_C * 12.0107) + (No_O * 15.9994), 'grams/mole')
