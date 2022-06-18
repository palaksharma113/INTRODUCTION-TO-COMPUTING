#Question 1
#To reverse the given string

#We take string as input from the user
s=input("Enter a string :")
l=len(s)
s2=''
for i in range(l-1,-1,-1):
    s2=s2+s[i] #Concatenating characters starting from the back of the input string to a new string
print("Reversed string is",s2)
