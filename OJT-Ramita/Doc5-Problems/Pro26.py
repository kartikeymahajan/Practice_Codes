'''26.Check sum of 2 numbers from given list which matches target value and returns the indexes 
of those numbers in the form of list.
l1 = [ 7,8,2,3,6,9,2,8]
Target = 14

O/p should be: [1,4]
Note : We should not be using more than 1 loop.'''

l1 = [ 7,8,2,3,6,9,2,10]
target = 19
start = 0
end = (len(l1))

def findTarget(l1,target, start, end):
    temp = l1[start]
    for i in range(start + 1, end):
        if temp + l1[i] == target:
            return [start, i]
    else:
        return findTarget(l1, target, start+1, end)

obj = findTarget(l1, target, start, end)
print(obj)


    
        