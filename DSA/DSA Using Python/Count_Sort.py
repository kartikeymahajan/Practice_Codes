def CountSort(arr):
    n = len(arr)
    maxsize = max(arr)
    carray = [0 for i in range(maxsize+1)]
    for i in range(n):
        carray[arr[i]] = carray[arr[i]]+1
    i, j = 0, 0
    while i < maxsize+1:
        if carray[i]>0:
            arr[j]=i
            j+=1
            carray[i] = carray[i]-1
        else:
            i+=1

li = [3,5,8,9,6,2]
print('Original Array:',li)
CountSort(li)
print('Sorted Array:',li)