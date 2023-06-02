'''2.Write a program in Python to remove duplicate elements form array without 
using inbuilt function.'''

li = [2,2,9,3,4,4,7,7,7,3,5]
# new_li = []
# for i in li:
#     if i not in new_li:
#         new_li.append(i)
# print(new_li)

def removeDuplicates(li):
    istart = 0
    iend = len(li)
    while istart < iend:
        temp = li[istart]
        jstart = istart + 1
        while jstart < iend:
            if li[jstart] == temp:
                li.remove(li[jstart])
                iend -= 1
                jstart -= 1
                istart -= 1
            jstart += 1
        istart += 1
    print(li)

removeDuplicates(li)