'''22. Write a function is_iterator so that it accepts an iterable and returns True if the
given iterable is an iterator.
is_iterator(iter([]))
True
>>> is_iterator([1, 2])
False'''


lis1 = [1, 2, 3, 4, 5]
temp = iter(lis1)

def is_iterator(li):
    return type(li) == type(iter(li))

obj = is_iterator(temp)
print(obj)
