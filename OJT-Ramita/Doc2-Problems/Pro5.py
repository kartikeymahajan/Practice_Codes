'''5. Write a function that accepts an iterable and returns a new iterable with all items
from the original iterable except for duplicates.
Ex. uniques_only([1, 2, 2, 1, 1, 3, 2, 1])
[1, 2, 3]'''


def findUnique(li):
    return list(set(li))

li = [1, 2, 2, 1, 1, 3, 2, 1]
obj = findUnique(li)
print(obj)