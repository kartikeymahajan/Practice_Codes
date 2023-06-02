li = [0,1,0,2,1,0,1,3,2,1,2,1]
def func(li):
    water = 0
    counter1 = 0
    for i in range(len(li)-1):
        if li[i]>li[i+1]:
            current = li[i]
            # flag = True
            for j in range(i+2, len(li)):
                water += current - li[j-1]
                if li[j]>=current:
                    # flag = False
                    break
                if j == len(li)-1:
                    water = 0
    return water

obj = func(li)
print(obj)

li = [0,1,0,2,1,0,1,3,2,1,2,1]
def func(li):
    water = 0
    counter1 = 0
    while counter1 < len(li)-1:
        if li[counter1]>li[counter1+1]:
            current = li[counter1]
            # flag = True
            for j in range(counter1+2, len(li)):
                water += current - li[j-1]
                if li[j]>=current:
                    counter1 = j-1
                    # flag = False
                    break
                if j == len(li)-1:
                    water = 0
        counter1 += 1
    return water

