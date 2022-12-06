def insertionsort(list):
    n = len(list)
    for i in range(1,n):
        cvalue = list[i]
        position = i
        while position > 0 and list[position-1] > cvalue:
            list[position] = list[position-1]
            position = position - 1
        list[position] = cvalue


list = [3,5,8,9,6,2]
print('Original Array:',list)
insertionsort(list)
print('Sorted Array:',list)