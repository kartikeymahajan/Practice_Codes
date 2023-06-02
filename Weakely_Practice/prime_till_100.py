
def prime_between(rangeTo: int):   
    li = [] 
    count = 0
    for num in range(rangeTo+1): #Traversing through given range.
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

obj = prime_between(10)
print(obj)


