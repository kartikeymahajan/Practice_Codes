'''3 Define logic for identifying the even numbers and odd numbers from the given list 
and generate a dictionary as follows
numbers= [4,5,7,2,9,8]
result	= {"even":[4,2,8],"odd":[5,7,9]}'''

numbers= [4,5,7,2,9,8]

result = {"even":[],"odd":[]}

for i in numbers:
    if i % 2 == 0:
        result["even"].append(i)
    else:
        result["odd"].append(i) 

print(result)


