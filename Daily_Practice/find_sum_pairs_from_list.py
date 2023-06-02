lst = [1,2,3]
def findPairs(lst, K): 
    # res = []
    count = 0
    while lst:
        num = lst.pop()
        diff = K - num
        if diff in lst:
            # res.append((diff, num))
            count+=1
          
    # res.reverse()
    return count

print(findPairs(lst, 3))