num = 7

flag = False

if num < 2:
    print("is not prime")
else:
    for i in range(2, num):
        if num%i==0:
            flag = True
            break
    if flag:
        print("is not prime")
    else:
        print("is prime")