'''18. Print the below rohmbus pattern according to the given number
for eg: given number is 4 then o/p will be: 
1
212
32123
4321234
32123
212
1  
'''

n = 7

numberofColumns = 1
for i in range(1,n+1):
    if i < 4:
        start = i
    else:
        start = 8 - i
    for j in range(1, numberofColumns+1):
        middleColumn = numberofColumns / 2 + 1
        print(start, end=" ")
        if j<middleColumn:
            start -= 1
        else:
            start += 1
    print()
    if i<4:
        numberofColumns += 2
    else:
        numberofColumns -= 2