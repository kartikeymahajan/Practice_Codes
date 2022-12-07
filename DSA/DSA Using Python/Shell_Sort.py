def ShellSort(list):
    n = len(list)
    gap=n//2
    while gap > 0:
        i = gap
        while i < n:
            temp = list[i]
            j = i - gap
            while j>=0 and list[j]>temp:
                list[j+gap]=list[j]
                j = j-gap
            list[j+gap]=temp
            i += 1
        gap = gap // 2

list = [3,5,8,9,6,2]
print('Original Array:',list)
ShellSort(list)
print('Sorted Array:',list)