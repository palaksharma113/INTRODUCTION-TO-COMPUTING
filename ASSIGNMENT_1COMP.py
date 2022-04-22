#Question 1: Find the average of three numbers entered by the user.

number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
number_3 = int(input("Enter the third number: "))

#Average
Average = (number_1 + number_2 + number_3)/3
print("The Average of three numbers is:\n", Average)

#Question 2: Compute a person's income tax (in $).

#To compute a person's income tax (in $)
Gross_income = float(input("Enter the gross income:\n"))

#There is a $10000 standard deduction.
Standard_deduction = 10000

No_of_dependents = int(input("Enter the number of dependents:\n"))

#There is a $3000 deduction for each dependent.
Dependent_deduction = 3000

Taxable_income = Gross_income - Standard_deduction - (Dependent_deduction * No_of_dependents)
print("Taxable_income:\n", Taxable_income)

#Tax rate = 20%

Tax = (Taxable_income * 20)/100
print("Tax: \n", Tax)
14  


#Question :3 Store different data type values into a list.

Name = input("Enter the name of the Student: ")
SID = int(input("Enter the Student ID:"))
Gender = input("Enter the gender of the Student(F,M,U): ")
Course_name = input("Enter the Student's course name: ")
CGPA = float(input("Enter the Student's CGPA: "))

Student_list = ['Name','SID','Gender','Course_name','CGPA']
print(Student_list)

Student_info = [Name,SID,Gender,Course_name,CGPA]
print("\n The list of the student information:\n ",Student_info)

 
#Question 4: Make a list to enter marks of five students and display them in a sorted manner.

Student1_marks = int(input("Enter the marks of the Student 1: "))
Student2_marks = int(input("Enter the marks of the Student 2: "))
Student3_marks = int(input("Enter the marks of the Student 3: "))
Student4_marks = int(input("Enter the marks of the Student 4: "))
Student5_marks = int(input("Enter the marks of the Student 5: "))

Student_markslist = [Student1_marks, Student2_marks, Student3_marks, Student4_marks, Student5_marks]
print("\n List of the Student Marks:\n ", Student_markslist)

#Sorted list
print("\n Sorted Student List (increasing order): ")
Student_markslist.sort()
print(Student_markslist)
