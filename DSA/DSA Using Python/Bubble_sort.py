def BubbleSort(list):
    n = len(list)
    for i in range(n-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp = list[j]
                list[j]=list[j+1]
                list[j+1]=temp

li = [3,5,8,9,6,2]
print('Original Array:',li)
BubbleSort(li)
print('Sorted Array:',li)