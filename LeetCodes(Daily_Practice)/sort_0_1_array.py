# input= [1, 0, -1, -1, 1, 0, 1, 0]
# import numpy as np

# def selection_sort(x):
#     for i in range(len(x)):
#         swap = i + np.argmin(x[i:])
#         print(swap)
#         (x[i], x[swap]) = (x[swap], x[i])
#     return x

# op = selection_sort(input)
# print(op)


l= [1, 0, -1, -1, 1, 0, 1, 0]
l1=[]
for i in range(len(l)):
    a=min(l)
    l1.append(a)
    l.remove(a)
print(l1)