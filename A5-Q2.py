# Question - 2

# print() creates a space inbetween lines while execution of codes making them easier to read
print()
range_1 = int(input("Enter the initial number of range :\n"))
print()
range_2 = int(input("Enter the last(ending) number of range :\n"))
print()
a = 1
number = int(input("Enter the divisor for entered range :\n"))

print()

print("Numbers divisile in the range are :")

for i in range(range_1,range_2):
    if i % number == 0:
        print(a,")",i)
        print()
    else:
        continue
    a = a + 1 
    
