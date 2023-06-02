"""8) Create a dictionary where the key is the number from the given list and the value
will be the occurrence of that element in the list. input= [1,2,3,2,4,2,4,7,8,4,5,8,6,9,2]"""

def CreateDict(input):
    di = {}
    for i in input:
        if i not in di:
            di[i] = 1
        else:
            di[i] += 1
    return di

input = [1,2,3,2,4,2,4,7,8,4,5,8,6,9,2]
obj = CreateDict(input)
print(obj)