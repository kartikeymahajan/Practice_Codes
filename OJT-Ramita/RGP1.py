'''1) Write a python program to right rotate a List by n
Enter position to rotate list item: 3
Sample input: [10, 20, 30, 40, 50, 60, 70]
Expected output: [50, 60, 70, 10, 20, 30, 40]'''

import time
import random

li = li =[2,3,-5,-7,9,4,6,-1,-8,0]
#[random.randrange(1,100,1) for i in  range(10000)]
def sortList(li):
    for i in range(len(li)-1):
        for j in range(i,len(li)-1):
            temp = li[i]
            if li[i]>li[j]:
                li[i] = li[j]
                li[j] = temp
            

print(time.time())
sortList(li)
print(time.time())
print(li)