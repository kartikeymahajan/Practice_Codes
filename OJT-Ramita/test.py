

def find_armstrong(num):
    st = str(num)
    temp = 0
    for j in st:
        temp += int(j)**3
    if temp == num:
        print(temp)
    
for i in range(1, 1000):
    find_armstrong(i)
