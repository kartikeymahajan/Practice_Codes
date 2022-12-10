def QuickSort(arr, low, high):
    if low < high:
        pi = Partision(arr, low, high)
        QuickSort(arr, low, pi-1)
        QuickSort(arr, pi+1, high)

def Partision(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    while True:
        while(i <= j)and(arr[i]<=pivot):
            i += 1
        while(i <= j)and(arr[j] > pivot):
            j -= 1
        if i <= j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        else:
            break
    temp = arr[low]
    arr[low] = arr[j]
    arr[j] = temp
    return j

li = [3,5,8,9,6,2]
print('Original Array:',li)
QuickSort(li, 0, len(li)-1)
print('Sorted Array:',li)