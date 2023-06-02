'''6) Write a python program to right rotate a List by n
Enter position to rotate list item: 3
Sample input: [10, 20, 30, 40, 50, 60, 70]
Expected output: [50, 60, 70, 10, 20, 30, 40]'''

def rotateList(li:list[int], item:int)->list:
    op = []
    for i in range(len(li)-item, len(li)):
        op.append(li[i])
    for i in range(0,len(li)-item):
        op.append(li[i])
    return op

li = [10, 20, 30, 40, 50, 60, 70]
item = 2
obj = rotateList(li,item)
print(obj)