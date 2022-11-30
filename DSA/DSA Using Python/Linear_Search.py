li = [2,6,3,7,4,9,1]

def findelement(li, element):
    index = 0
    while index < len(li):
        if li[index]==element:
            return index
        index+=1
    return -1

op = findelement(li, 78)
print(op)