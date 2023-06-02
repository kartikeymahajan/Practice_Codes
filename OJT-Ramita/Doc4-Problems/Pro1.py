'''1.Sort the below list without using inbuilt function I = [2,3,-5,-7,9,4,6,-1,-8,0]'''

li =[2,3,-5,-7,9,4,6,-1,-8,0]

for i in range(len(li)):
    for j in range(i,len(li)):
        if li[i] > li[j]:
            li[i], li[j] = li[j], li[i]

print(li)