'''23. create 2 dictionaries as follows:
dict1 = {'name': 'Msys','Place': 'Pune'}
dict2 = {'EmpID': 0001, 'Salary': 50000}
Perform following operations:
a. create single dictionary by merging dict1 & dict2
b. update the salary to 10%
c. update age to 35
d. extract & print all the values & keys separetly in tuple.
e. delete the element with key 'Age' & print the dictionary elements.'''

dict1 = {'name': 'Msys','Place': 'Pune'}
dict2 = {'EmpID': '0001', 'Salary': 50000}

# a. create single dictionary by merging dict1 & dict2
singleDict = (dict1 | dict2)
print(singleDict)

# b. update the salary to 10%
temp = singleDict["Salary"] / 10
singleDict["Salary"] += int(temp)
print(singleDict)

# c. update age to 35
singleDict['Age'] = 35
print(singleDict)

# d. extract & print all the values & keys separetly in tuple.
keys = singleDict.keys()
values = singleDict.values()
print(tuple(keys))
print(tuple(values))

# e. delete the element with key 'Age' & print the dictionary elements.
singleDict.pop('Age')
print(singleDict)