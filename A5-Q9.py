#Question 9
#Count the number of occurrence of each word in the list input by the user

str=input("Enter a string: ")
#Empty dictionary is created to 
counts = dict()
#We split the input string into words and store it in in a list
words = str.split(' ')
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)
