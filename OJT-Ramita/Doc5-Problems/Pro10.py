'''10.Sort the list of integers in descending order without using inbuilt functions . 
lst = [56,2,13,1,78,4,6]'''

lst = [56,2,13,1,78,4,6]

for i in range(len(lst)):
    for j in range(i, len(lst)):
        if lst[j]>lst[i]:
            lst[j], lst[i] = lst[i], lst[j]

print(lst)