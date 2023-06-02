'''28. Write a Python program to remove the parenthesis area in a string using Regular
Expression
Sample data : [example (.com), "MSys", github (.com), keka (.com)]
Expected Output:
Example
MSys
github
keka'''
 

data = ["example (.com)", "MSys", "github (.com)", "keka (.com)"]

for i in data:
    temp = i.split("(")
    print(temp[0])

