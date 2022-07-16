# ASSIGNMENT-7



# QUESTION-1
# GST CALCULATOR

from tkinter import *

def find_gst(): # function to calculate GST rate
    org_cost=int(cost_val.get()) # getting input of original cost and net price
    net_price=int(price_val.get())
    rate=(net_price-org_cost)*100/org_cost
    rate_val.insert(10, str(rate) + "%") # inserting GST rate in answer value

gui=Tk()
gui.title("GST Calculator")
gui.geometry("250x150")

cost=Label(gui, text="Original Cost: ") # variable for original cost
cost.grid(row=1, column=1)
price=Label(gui, text="Net Price: ") # variable for net price
price.grid(row=2, column=1)
rate=Label(gui, text="GST Rate: ") # variable for GST rate
rate.grid(row=4, column=1)

find=Button(gui, text="Find GST", command=find_gst) # button to find GST rate
find.grid(row=3, column=2)

cost_val=Entry(gui) # value for original cost
cost_val.grid(row=1, column=2)
price_val=Entry(gui) # value of net price
price_val.grid(row=2, column=2)
rate_val=Entry(gui) # value of GST rate
rate_val.grid(row=4, column=2)

gui.mainloop()



# QUESTION-2
# CALENDAR

from tkinter import *
import calendar

def show_cal(): # function to display calendar
    cal=Tk()
    cal.title("CALENDAR")
    cal.geometry("500x600")

    fetch_year=int(year_val.get()) # gets input of year
    cal_content=calendar.calendar(fetch_year) # fetches calendar of input year
    cal_year=Label(cal, text=cal_content)
    cal_year.grid(row=5, column=1)

    cal.mainloop()


cal_year=Tk()
cal_year.title("Calendar")
cal_year.geometry("250x150")

year=Label(cal_year, text="Enter Year: ")
year.grid(row=1, column=1)
year_val=Entry(cal_year) # takes input of year from user
year_val.grid(row=2, column=1)

show=Button(cal_year, text="Show Calendar", command=show_cal) # button to show year
show.grid(row=3, column=1)

cal_year.mainloop()



# QUESTION-3
# CALCULATOR

from tkinter import *

expression = ""
def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)

def equalpress():
	try:

		global expression
		total = str(eval(expression))
		equation.set(total)
		expression = ""
	except:
		equation.set(" error ")
		expression = ""

def clear():
	global expression
	expression = ""
	equation.set("")


my_calculator = Tk()

my_calculator.title("Calculator")
my_calculator.geometry("270x150")

equation = StringVar()
expression_field = Entry(my_calculator, textvariable=equation) # takes input of operation
expression_field.grid(columnspan=4, ipadx=70)

# buttons and their commands
button1 = Button(my_calculator, text=' 1 ', command=lambda: press(1), height=1, width=7)
button1.grid(row=2, column=0)

button2 = Button(my_calculator, text=' 2 ', command=lambda: press(2), height=1, width=7)
button2.grid(row=2, column=1)

button3 = Button(my_calculator, text=' 3 ', command=lambda: press(3), height=1, width=7)
button3.grid(row=2, column=2)

button4 = Button(my_calculator, text=' 4 ', command=lambda: press(4), height=1, width=7)
button4.grid(row=3, column=0)

button5 = Button(my_calculator, text=' 5 ', command=lambda: press(5), height=1, width=7)
button5.grid(row=3, column=1)

button6 = Button(my_calculator, text=' 6 ', command=lambda: press(6), height=1, width=7)
button6.grid(row=3, column=2)

button7 = Button(my_calculator, text=' 7 ', command=lambda: press(7), height=1, width=7)
button7.grid(row=4, column=0)

button8 = Button(my_calculator, text=' 8 ', command=lambda: press(8), height=1, width=7)
button8.grid(row=4, column=1)

button9 = Button(my_calculator, text=' 9 ', command=lambda: press(9), height=1, width=7)
button9.grid(row=4, column=2)

button0 = Button(my_calculator, text=' 0 ', command=lambda: press(0), height=1, width=7)
button0.grid(row=5, column=0)

plus = Button(my_calculator, text=' + ', bg='blue',
				command=lambda: press("+"), height=1, width=7)
plus.grid(row=2, column=3)

minus = Button(my_calculator, text=' - ', bg='blue',
				command=lambda: press("-"), height=1, width=7)
minus.grid(row=3, column=3)

multiply = Button(my_calculator, text=' * ', bg='blue',
					command=lambda: press("*"), height=1, width=7)
multiply.grid(row=4, column=3)

divide = Button(my_calculator, text=' / ', bg='blue',
					command=lambda: press("/"), height=1, width=7)
divide.grid(row=5, column=3)

equal = Button(my_calculator, text=' = ', bg='yellow',
				command=equalpress, height=1, width=7)
equal.grid(row=5, column=2)

clear = Button(my_calculator, text='Clear', bg='red',
				command=clear, height=1, width=7)
clear.grid(row=5, column='1')

Decimal= Button(my_calculator, text='.', bg='green',
					command=lambda: press('.'), height=1, width=7)
Decimal.grid(row=6, column=0)
	
my_calculator.mainloop()



# QUESTION-4
# SORTING LIST

list_size=int(input("Enter size of list: "))
marks=[] # list that will store marks
for i in range(0, list_size): # taking input of elements
    element=int(input("Enter marks: "))
    marks.append(element)

def partition(my_list, low, high): # function takes last element as pivot
    i=(low-1)
    pivot=my_list[high]
    for j in range(low, high): # sorts all elements smaller than pivot on its left and all elements greater on right side
        if my_list[j]<=pivot:
            i=i+1
            my_list[i], my_list[j]=my_list[j], my_list[i]
    my_list[i+1], my_list[high]=my_list[high], my_list[i+1]
    return (i+1)

def quick_sort(my_list, low, high): # function to do quick sort
    if len(my_list)==1:
        return my_list
    if low < high:
        pe=partition(my_list, low, high) # pe is partitioning element
        quick_sort(my_list, low, pe-1) # sorts elements before pe
        quick_sort(my_list, pe+1, high) # sorts elements after pe

quick_sort(marks, 0, list_size-1) # quick sort function is called for marks list
print(marks)



# QUESTION-5
# SORTING AND SEARCHING

array_size=int(input("Enter size of array: "))
array=[]
for i in range(0, array_size):
    element=int(input("Enter element "))
    array.append(element)

# PART-(a)
# Sorting the array
# Selection Sort Algorithm
for i in range(0, array_size):
    min_index=i
    for j in range(i+1, array_size):
        if array[min_index]>array[j]:
            min_index=j # finding minimum element
    array[i], array[min_index]=array[min_index], array[i] # swapping first element with minimum element
print(array)

x=int(input("Enter element to be searched and counted: "))

# PART-(b)
# Binary Search Algorithm
def binary_search(array, x):
    low=0
    high=len(array)-1
    mid=0
    while low<=high:
        mid=(high + low)//2
        if array[mid]<x: # if x is greater than mid element, ignore left half
            low=mid+1
        elif array[mid]>x: # if x is less than mid element, ignore right half
            high=mid-1
        else:
            return mid # this means x is present at mid position
    return -1 # in this case, x is not present

result=binary_search(array, x)
if result!=-1:
    print("Element is present at index", result)
else:
    print("Error! Element is not present.")

# PART-(c)
# Counting occurrences of element
def count(array, x): # function to count occurrences of element
    count=0
    for i in array:
        if i==x:
            count+=1
    return count

occurrences=count(array, x)
print("Number of occurrences of element is", occurrences)

#QUESTION 6
#REMOVING DUPLICATES AND SORTING

def selection_sort(array):  
    length = len(array)  
      
    for i in range(length-1):  
        minIndex = i  
          
        for j in range(i+1, length):  
            if array[j]<array[minIndex]:  
                minIndex = j  
                  
        array[i], array[minIndex] = array[minIndex], array[i]  
          
    return array
def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return
n=int(input("Enter number of inputs:"))
l=[]
for i in range(0,n):
    s=int(input("Enter number:"))
    l.append(s)
l=set(l)
l=list(l)
l.sort()
print(l)
