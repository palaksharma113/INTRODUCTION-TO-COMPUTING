# Question - 6

# First, we will take the input: 
# The upper value and lower value of range 
print()
lower_value = int(input ("Please, Enter the Lowest Range Value : \n"))  
upper_value = int(input ("Please, Enter the Upper Range Value : \n"))  

# Prime numbers are whose who only are divisible by :
# number 1 and themselves

a = 1

# print() creates a space inbetween lines while execution of codes making them easier to read
print()

print ("The Prime Numbers in the range are: ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (a,")",number)  
            a += 1

print()
