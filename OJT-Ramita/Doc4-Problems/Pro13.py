'''13.Let's assume there is function defined which expects only list as an argument, 
However there is chance that sometimes function will be called with different type of data, 
Now Fix this scenario to handle the other types without breaking the code ·'''

def takeList(li:list):
    if type(li) == list:
        print("valid argument")
    else:
        print("Invalid argument")

'''
•Scenario 1: If the argument provided is a list then, Print inside the function as 
"valid argument"· '''

print("Using Valid Data", end=": ")
li = [1,2,3,4,5]
takeList(li)

'''
•Scenario 2: if the argument provided is a different data type, then Print a message saying" 
invalid argument, You have provided data type (str/int)"'''

print("Using Invalid Data", end=": ")
st = "Msys"
takeList(st)