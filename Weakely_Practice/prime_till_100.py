
def prime_between(rangeFrom: int, rangeTo: int):   
    li = [] 
    for num in range(rangeFrom, rangeTo): #Traversing through given range.
        flag = True
        if num > 1:
            while flag:
                for i in range(2, num): 
                    if num % i == 0:
                        flag = False
                        break
                else:
                    li.append(num)
                    break
    return li

obj = prime_between(0,100)
print(obj)


