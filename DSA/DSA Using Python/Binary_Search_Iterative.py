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
    return "not found"

li = [12,45,65,76,83]
op = BinarySearch(li, 12)
print(op)
