def BinarySearch(list, element, left, right):
    if left > right:
        return -1
    else:
        mid = (left+right)//2
        if element == list[mid]:
            return mid
        elif element < list[mid]:
            return BinarySearch(list, element, left, mid-1)
        elif element > list[mid]:
            return BinarySearch(list, element, mid+1, right)

li = [12,45,65,76,83]
op = BinarySearch(li, 76, 0, len(li)-1 )
print(op)
        