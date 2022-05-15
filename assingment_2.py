#Question 1: Write Python code for the following:-

input_string = "Python is a case sensitive language"
print(input_string)
#(a) Find the length of the input string.
print('\n (a)')
print("The length of the input string: \n",len(input_string))

#(b) Reverse the order of the string in one line code.
print('\n (c)')
print("Reverse of the given input string: \n",input_string[ : :-1])

#(c) Using Slice function store "a case sensitive" in new string.
print('\n (c)')
new_string = input_string[10:26]
print("Store 'a case sensitive' in new string: \n ",new_string)

#(d) Replace "a case sensitive" with "object oriented".
print('\n (d)')
updated_string = input_string.replace("a case sensitive","object oriented")
print("Updated string after replacing 'a case sensitive' with 'object oriented': \n",updated_string)

#(e) Find index of substring "a" in the given input string.
print('\n (e)')
index_substring = input_string.index('a')
print("The index of substring 'a' in the given input string: \n",index_substring)

#(f) Remove the white spaces from the given input string.
print('\n (f)')
input_string = input_string.strip()
print("String after removing the white spaces from the given input string: \n",input_string)

#Question 2: Store your name, SID, department name and CGPA into different variables. With the help of String formatting print the following output:

Name = "Palak Sharma"
SID = 21102003
Department_name = "Civil"
CGPA = 9.9
print(f"\nHey, {Name} Here!\n"
      f"My SID is {SID} \n"
      f"I am from {Department_name} department and my CGPA is {CGPA}")

#Question 3: For a = 56 and b = 10 with the help of bitwise operators calculate the following:-

a = 56
b = 10
print('\n (a)')
print("With the help of bitwise AND operator :\n",a&b)
print('\n (b)')
print("With the help of bitwise OR operator:\n", a|b)
print('\n (c)')
print("With the help of bitwise XOR operator:\n", a^b)
print('\n (d)')
print("Bitwise Left shift a with 2 bits: \n",a<<2)
print("Bitwise Left shift b with 2 bits: \n",b<<2)
print('\n (e)')
print("Bitwise Right shift a with 4 bits: \n",a>>4)
print("Bitwise Right shift b with 4 bits: \n",b>>4)


#Question 4: Write a python program to check if the word “name” is present in the string entered by the user(Print : "Yes" or "No").

input_string = input("\nEnter the string:\n")
print("\nThe word 'name' is present in the entered string or not (Yes or No)?")

if 'name' in input_string:
    print("Yes \n")
else:
    print("No \n")

#Question 5 For any three lenght check whether it is possible to form a triangle or not.
    
Side_1 = int(input("Enter the first side of a triangle:\n"))
Side_2 = int(input("Enter the second side of a triangle:\n"))
Side_3 = int(input("Enter the third side of a triangle:\n"))
print("\nThe given input lengths can form a triangle or not (Yes or No)?")
while(Side_1 + Side_2 > Side_3) and (Side_2 + Side_3 > Side_1) and (Side_3 +Side_1> Side_2):
    print('Tringle is valid')
    break

#Question 6: Given two numbers ‘a’ and b’. Write a program to count number of bits needed to be flipped to convert ‘a’ to ‘b’.
a = int(input("enter a number:"))
b = int(input("enter a number:"))
num = a ^ b
Count_flipped_bit = 0
while (num != 0):
    num = num & (num - 1)
    Count_flipped_bit += 1
print("Number of bits needed to be flipped to convert a to b is:",Count_flipped_bit)
