'''17. Write a function that takes a sequence (like a list, string, or tuple) and a number n
and returns the last n elements from the given sequence, as a list. For example:
>>> tail([1, 2, 3, 4, 5], 3)
[3, 4, 5]'''

def fetchLast(iter,n):
    temp = len(iter) - n
    return iter[temp:]

iter = [1, 2, 3, 4, 5]
n = 3
obj = fetchLast(iter,n)
print(obj)