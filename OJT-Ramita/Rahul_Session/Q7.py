l = [10, 2, 9, 9, 8, 3, 9]
n = 8

def findSumIndex(lst, n):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == n:
                return [i, j]

obj = findSumIndex(l, n)
print(obj)