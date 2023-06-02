l = [[4,9,8], [6,2,1], [3,4,2]]
count = 1
f = 0
s = 1
t = 2
while count < 4:
    print(l[0][f],l[1][s],l[2][t])
    f += 1
    s += 1
    t += 1
    if f > 2:
        f = 0
    elif s > 2:
        s = 0
    elif t > 2:
        t = 0
    count += 1