def RadixSort(arr):
    n = len(arr)
    maxelement = max(arr)
    digits = len(str(maxelement))
    l = []
    bins = [l]* 10
    for i in range(digits):
        for j in range(n):
            e = int((arr[j]/pow(10,i))%10)
            if len(bins[e])>0:
                bins[e].append(arr[j])
            else:
                bins[e] = [arr[j]]
        k = 0
        for x in range(10):
            if len(bins[x])>0:
                for y in range(len(bins[x])):
                    arr[k] = bins[x].pop(0)
                    k = k+1

li = [63,250,835,947,651,28]
print('Original Array:',li)
RadixSort(li)
print('Sorted Array:',li)