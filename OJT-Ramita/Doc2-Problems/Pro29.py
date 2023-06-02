'''29. Write a function called interleave which accepts two iterables of any type and
returns a new iterable with each of the given items "interleaved" (item 0 from
iterable 1, then item 0 from iterable 2, then item 1 from iterable 1, and so on).'''

li1 = [3,6,2,89,5,4,6,8,9]
li2 = [45,34,76,45]

def combine(li1, li2):
    
    output = []

    if len(li1)<len(li2):
        small = li1
        big = li2
    else:
        small = li2
        big = li1

    for i in range(len(small)):
        output.append(li1[i])
        output.append(li2[i])
    
    if len(big) != len(small):
        temp = len(big) - len(small)
        output.extend(big[-temp:])

    return output

obj = combine(li1, li2)
print(obj)