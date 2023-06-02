num = 19
def isHappy(num):
    arr = set()
    while num != 1:
        str_num = str(num)
        num = 0
        for i in str_num:
            num += int(i)**2
    
        if num in arr:
            return False
        else:
            arr.add(num)
    else:
        return True
obj = isHappy(num)
print(obj)