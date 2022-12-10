def MergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        MergeSort(arr, left, mid)
        MergeSort(arr, mid+1, right)
        Merge(arr, left, mid, right)

def Merge(arr, left, mid, right):
    i = left 
    j = mid+1
    k = left
    temp = [0]*(right+1)
    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k +=1
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
        for x in range(left, right + 1):
            arr[x] = temp[x]

list = [3,5,8,9,6,2]
print('Original Array:',list)
MergeSort(list, 0, len(list)-1)
print('Sorted Array:',list)