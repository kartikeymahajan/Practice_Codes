'''3. Write a function called interleave which accepts two iterables of any type and
returns a new iterable with each of the given items "interleaved" (item 0 from
iterable 1, then item 0 from iterable 2, then item 1 from iterable 1, and so on). An
assumption here that both iterables contain the same number of elements.'''

def interleave(li1, li2):
    output = []
    for i in range(len(li1)):
        output.append(li1[i])
        output.append(li2[i])
    return output

li1 = [1,3,5,7,9]
li2 = [2,4,6,8,10]

obj = interleave(li1, li2)
print(obj)