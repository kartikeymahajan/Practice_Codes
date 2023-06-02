import time
def BinarySearch(li, element):
    l = 0
    r = len(li)-1
    while l <= r:
        m = (l + r)//2
        if element == li[m]:
            return m
        elif element < li[m]:
            r = m-1
        elif element > li[m]:
            l = m+1
    return "ElementNotExists"

li = [2,3,7,12,17,23,45,70]
# t = time.time()
op = BinarySearch(li, 4)
print(op)
# print(time.time() - t)
