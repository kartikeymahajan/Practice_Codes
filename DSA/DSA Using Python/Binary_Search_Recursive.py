import time
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

li = [2,3,7,12,17,23,45,70]
t = time.time()
op = BinarySearch(li, 45, 0, len(li)-1 )
print(op)
print(time.time() - t)
        