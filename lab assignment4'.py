#Q.1
m=int(input("Enter Marks :"))
if(m<25):
    print(" Grade F ")
elif(m>=25 and m<45):
    print(" Grade E ")
elif(m>=45 and m<50):
    print(" Grade D ")
elif(m>=50 and m<60):
    print(" Grade C ")
elif(m>=60 and m<80):
    print(" Grade B ")
elif(m>=80):   
    print(" Grade A ")
else:
    print(" No result ")

#Q.2
year = int(input("Enter a year: "))

if year % 4 == 0 :
    print("year is a Leap Year")
elif year % 100 == 0 :
    print("year is not a Leap Year")
elif year % 400 == 0 :
    print(" year is a Leap Year")
else :
    print("year is not a Leap Year")

#Q.3
import random
for i in range(10):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    print(f"Question {i+1}:",end="")
    user_output = int(input(f"{num1}X{num2}="))
    if user_output == (num1*num2):
        print("Right!")
    else:
        print(f"Wrong.The right answer is {num1*num2}")
    

#Q.4
x=200

for candies in range(x):

    if candies % 5 == 2:
       if candies % 6 == 3:
          if candies % 7 == 2:
             print(candies, 'candies are in the bowl!')
             break
