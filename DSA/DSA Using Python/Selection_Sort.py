def SelectionSort(ls: list[int])->list [int]:
    n = len(ls)
    for i in range(n-1):
        position = i
        for j in range(i+1, n):
            if ls[j]<ls[position]:
                position = j
        ls[i], ls[position] = ls[position], ls[i]
    return ls
l=[23,5,36,74,13,74,93,23,56,82,45]
op = SelectionSort(l)
print(op)