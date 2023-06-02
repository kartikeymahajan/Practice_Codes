'''11.From the given list, check if the element is an integer then return square of that 
element and if element is a string then return the same string 2 times. Output should be in 
list format.

a = [8,9,10,"f",5,8,"d"]
Output should be : [64, 81, 100, 'ff', 25, 64, 'dd']'''

a = [8,9,10,"f",5,8,"d"]
result = []

for i in a:
    if type(i) == int:
        result.append(i*i)
    elif type(i)== str:
        result.append(i*2)

print(result)

