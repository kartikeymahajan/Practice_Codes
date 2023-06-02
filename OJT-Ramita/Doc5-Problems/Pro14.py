'''14.In the given list, check if the element is None, replace it with the recent value . 
l = [1,None,None,3,None,4]
Output should be : [1,1,1,3,3,4]'''

l = [1,None,None,3,None,4]
result = []

for i in l:
    if i != None:
        temp = i
        result.append(i)
    else:
        result.append(temp)

print(result)
